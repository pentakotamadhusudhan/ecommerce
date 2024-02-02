import json
from genericresponse import GenericResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from partners.serializer import PharmacySerializer
from errormessage import Errormessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import get_template
from partners.models import PharmacyModel
from django.shortcuts import render
from django.apps import apps
import datetime

class PharmacyRegisterAPI(generics.GenericAPIView):
    serializer_class = PharmacySerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                #RegisterUsername=request.data.get('RegisterUsername')
                PharmacyName = request.data.get('PharmacyName')
                Email = request.data.get('PharmacyEmailId')
                # Firstname = request.data.get('Firstname')
                # Lastname = request.data.get('Lastname')
                #otp=generateOTP()
                # print(otp)
                created_at=datetime.datetime.now()
                print(created_at)
                print(user.id)
                #user1 = EmailVerifyTable(UserId_id=user.id, otp=otp).save()
                htmly = get_template('clinicreg.html')
                d = {'created_at': created_at,"PharmacyName":PharmacyName}
                subject, from_email, to = 'Confirmation mail for Registration',  settings.FROM_EMAIL, Email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content,  settings.FROM_EMAIL, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = PharmacySerializer(user).data
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




