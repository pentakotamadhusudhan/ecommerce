import json

from django.template.defaultfilters import title
from djongo.base import logger
from rest_framework import generics
from rest_framework import generics
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from partners.serializer import TypeOfPartnerSerializer
from genericresponse import GenericResponse
# from partners.models import ClinicProfileSerializer
from django.apps import apps

from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class TypeOfPartnerAPI(generics.GenericAPIView):
    serializer_class = TypeOfPartnerSerializer

    def post(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = TypeOfPartnerSerializer(user).data
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





