from rest_framework import generics
from django.apps import apps
from rest_framework.response import Response
from hcpapi.serializer import HcpClinicSerializer
from genericresponse import GenericResponse
import json
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class HcpClinicRegAPI(generics.GenericAPIView):
    serializer_class = HcpClinicSerializer

    def post(self, request, *args, **kwargs):
        HcpEmail = apps.get_model("hcpapi", "HcpModel")
        hcpId = request.data.get("HcpId")
        emailData = HcpEmail.objects.get(id=hcpId)
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            htmly = get_template('addclinic.html')
            d = {'Firstname':emailData.Firstname,'Lastname':emailData.Lastname}
            subject, from_email, to = 'Your Clinic Is successfully added', settings.FROM_EMAIL, emailData.Email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = HcpClinicSerializer(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)