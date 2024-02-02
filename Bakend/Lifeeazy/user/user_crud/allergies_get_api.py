import json

from django.template.defaultfilters import title
from djongo.base import logger
from rest_framework import generics
from rest_framework import generics
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import AlergiesPostSerializer
from genericresponse import GenericResponse
from user.models import Alergies
from django.apps import apps

from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class AllergiesGetApi(generics.GenericAPIView):
    serializer_class=AlergiesPostSerializer

    def get(self,request):
        try:
            data = Alergies.objects.all()
            serializer_class = AlergiesPostSerializer(data, many=True)
            if serializer_class.data:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = serializer_class.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
