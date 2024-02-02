from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import AnthropometricsGetSerializer
from user.models import AnthropometricsModel


class AnthropometricsGetByFamilyById(generics.GenericAPIView):
    serializer_class = AnthropometricsGetSerializer

    def get(self, request, FamilyId):
        if AnthropometricsModel.objects.filter(FamilyId=FamilyId):
            result = AnthropometricsModel.objects.filter(FamilyId=FamilyId)
            prodata = AnthropometricsGetSerializer(result, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = prodata.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Family Id doesnt exist"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)