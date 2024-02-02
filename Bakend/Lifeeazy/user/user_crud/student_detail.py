import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import UserSerializer
from user.models import UserModel

class StudentDetail(APIView):
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, MobileNumber):
        if MobileNumber:
            try:
                res = UserModel.objects.get(MobileNumber=MobileNumber)
                output = UserSerializer(res).data
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = output
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
                # return Response({'message': 'Successful',
                #                  'Result': output,
                #                  'HasError': False,
                #                  'status': 200})

            except UserModel.DoesNotExist:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "you haven't registered"
                response.Result = ""
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
                # return Response({'message': 'you havent registered',
                #                  'Result': False,
                #                  'HasError': True,
                #                  'status': 400})
