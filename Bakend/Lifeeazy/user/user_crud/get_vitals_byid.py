from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import GetVitalSerializer
from user.models import VitalsModel


class GetVitalsByUserId(generics.GenericAPIView):
    serializer_class = GetVitalSerializer

    def get(self, request, UserId):
        if VitalsModel.objects.filter(UserId=UserId):
            result = VitalsModel.objects.filter(UserId=UserId)
            prodata = GetVitalSerializer(result, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = prodata.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "UserModel matching query does not exist"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
