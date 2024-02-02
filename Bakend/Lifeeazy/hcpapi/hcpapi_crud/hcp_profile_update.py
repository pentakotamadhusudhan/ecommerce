from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpProfileUpdateSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpProfile
from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.apps import apps


class HcpProfileUpdate(generics.GenericAPIView):
    serializer_class = HcpProfileUpdateSerializer

    def put(self, request, HcpId):

        try:
            r = HcpProfile.objects.get(HcpId=HcpId)
            HcpEmail = apps.get_model("hcpapi", "HcpModel")

            emailData = HcpEmail.objects.get(id=HcpId)

            email = emailData.Email
            Firstname=emailData.Firstname
            Lastname=emailData.Lastname

            ProfilePicture=request.data.get("ProfilePicture")
            state = request.data.get("State")
            city = request.data.get("City")
            address = request.data.get("Address")
            pincode = request.data.get("Pincode")
            timezone = request.data.get("Timezone")
            data = {'ProfilePicture':ProfilePicture,'State': state, 'City': city, 'Address': address, 'Pincode': pincode, 'Timezone': timezone}
            s = HcpProfileUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Username = request.data.get('Username')
            htmly = get_template('hcp_profile_update.html')
            d = {'Username': Username,"Firstname":Firstname,"Lastname":Lastname}
            subject, from_email, to = 'You have Successfully Updated the Profile', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except HcpProfile.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
