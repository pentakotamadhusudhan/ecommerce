from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpClinicSerializer,HcpClinicUpdateSerializer
from genericresponse import GenericResponse
from hcpapi.models import Clinic
import json
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from errormessage import Errormessage


class HcpClinicUpdate(generics.GenericAPIView):
    serializer_class = HcpClinicUpdateSerializer

    def put(self, request, HcpId):
        try:
            r = Clinic.objects.get(HcpId=HcpId)
            HcpEmail = apps.get_model("hcpapi", "HcpModel")
            emailData = HcpEmail.objects.get(id=HcpId)

            email = emailData.Email
            Firstname = emailData.Firstname
            Lastname = emailData.Lastname
            ClinicName = request.data.get("ClinicName")
            Address = request.data.get("Address")
            FromDate=request.data.get("FromDate")
            ToDate = request.data.get("ToDate")
            FromTime = request.data.get("FromTime")
            ToTime = request.data.get("ToTime")
            Fee = request.data.get("Fee")
            data = {'ClinicName': ClinicName, 'Address': Address,'FromDate':FromDate, 'ToDate': ToDate, 'FromTime': FromTime,
                    'ToTime': ToTime, 'Fee': Fee}
            s = HcpClinicUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            Username = request.data.get('Username')
            htmly = get_template('updateclinic.html')
            d = {'Username': Username,'Firstname':Firstname,'Lastname':Lastname}
            subject, from_email, to = 'Clinic Updated', settings.FROM_EMAIL, email
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
        except Clinic.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)