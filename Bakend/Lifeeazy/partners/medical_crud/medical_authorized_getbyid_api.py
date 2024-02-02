import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from partners.serializer import MedicalAutherizedSerializer
from partners.models import MedicalAuthorizedModel
from errormessage import Errormessage


class MedicalAuthorizedGetById(APIView):
    serializer_class = MedicalAutherizedSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request,Id):
        try:
            result = MedicalAuthorizedModel.objects.filter(medicalid=Id)
            serializer_class = MedicalAutherizedSerializer(result, many=True)
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