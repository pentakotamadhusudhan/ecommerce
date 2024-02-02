from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import AnthropometricsGetSerializer
import json
from user.models import AnthropometricsModel


class AnthropometricsGetByUserId(generics.GenericAPIView):
    serializer_class = AnthropometricsGetSerializer

    def get(self, request, UserId):
        try:
            result = AnthropometricsModel.objects.filter(UserId=UserId)
            serializer_class = AnthropometricsGetSerializer(result, many=True)

            if serializer_class.data:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "User data not found"
                response.Result = []
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "User data not found"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)