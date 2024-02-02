from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpPasswordSerializer,generateOTP
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpModel,HcpOtpModel
from errormessage import Errormessage
import datetime
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class HcpChangePasswordView(generics.GenericAPIView):
    serializer_class = HcpPasswordSerializer

    def put(self, request, HcpId):
        try:
            r = HcpModel.objects.get(id=HcpId)
            password = make_password(request.data.get("Password"))
            data = {'Password': password}
            s = HcpPasswordSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            #HcpEmail = apps.get_model("hcpapi", "HcpModel")
           # hcpId = request.data.get("HcpId")
            emailData = HcpModel.objects.get(id=HcpId)

            email = emailData.Email
            Firstname=emailData.Firstname
            Lastname=emailData.Lastname

            otp = generateOTP()
            print(otp)
            created_at = datetime.datetime.now()
            print(created_at)
            user1 = HcpOtpModel(HcpId_id=HcpId, otp=otp).save()
            htmly = get_template('hcp_registration_otp.html')
            d = {'otp': otp, 'created_at': created_at,"Firstname":Firstname,"Lastname":Lastname}
            subject, from_email, to = 'Changed password successfully', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except HcpModel.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

