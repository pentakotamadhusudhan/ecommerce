import json

from django.template.defaultfilters import title
from djongo.base import logger
from rest_framework import generics
from rest_framework import generics
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import HcpProfileSerializer
from genericresponse import GenericResponse
from hcpapi.models import HcpProfile
from django.apps import apps

from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class HcpProfileAPI(generics.GenericAPIView):
    serializer_class = HcpProfileSerializer

    def post(self, request, *args, **kwargs):

        try:
            HcpEmail = apps.get_model("hcpapi", "HcpModel")
            hcpId = request.data.get("HcpId")
            emailData = HcpEmail.objects.get(id=hcpId)

            email = emailData.Email
            Firstname = emailData.Firstname
            Lastname = emailData.Lastname

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            Username = request.data.get('Username')
            htmly = get_template('hcp_profile_add.html')
            d = {'Username': Username, "Firstname": Firstname, "Lastname": Lastname}
            subject, from_email, to = 'Your Profile is been Added Successfully', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = HcpProfileSerializer(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            if e:
                response.Message = [Errormessage(e), str(e)]
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
            else:
                pass
