import json
from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import ClinicSerializer
from genericresponse import GenericResponse
from errormessage import Errormessage
from django.template.loader import get_template
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from testapp.serializer import TestSerializer
from errormessage import Errormessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import get_template
from user.models import EmailVerifyTable
from django.shortcuts import render
from django.apps import apps
import datetime

class Testpost(generics.GenericAPIView):
    serializer_class = TestSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = TestSerializer(user).data
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




