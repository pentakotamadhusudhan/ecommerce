import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import GetMedicalSumSerializer
from user.models import UserModel
from errormessage import Errormessage


class GetAllMedicalSummery(APIView):
    QuerySet = GetMedicalSumSerializer
    renderer_classes = [JSONRenderer]


    def get(self, request):
        try:
            result = UserModel.objects.all()
            prodata = GetMedicalSumSerializer(result, many=True)
            return Response({
                "Message":"Successful",
                "result":prodata.data,
            })
            # response = GenericResponse("Message", "Result", "Status", "HasError")
            # response.Message = "Successful"
            # response.Result = prodata.data
            # response.Status = 200
            # response.HasError = False
            # jsonStr = json.dumps(response.__dict__)
            # return Response(json.loads(jsonStr), status=200)
        except UserModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)