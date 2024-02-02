import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import FCMSerializers
# from user.models import UserDependentEmergencyDetails


from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from firebase import FCMF_token

from user.serializers import FCMSerializers
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from firebase import FCMF_token


class FCMApi(generics.GenericAPIView):
    serializer_class = FCMSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        title = request.data.get('title')
        body = request.data.get('body')
        DeviceToken = request.data.get('DeviceToken')
        user = FCMF_token(title, body, DeviceToken)
        response = GenericResponse("message", "result", "status", "has_error")
        response = GenericResponse("Message", "Result", "Status", "HasError")
        response.Message = "Successful"
        response.Result = user
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)
        # return Response({
        #     'message': 'Successful',
        #     'Result': user,
        #     'HasError': False,
        #     'status': 200
        #
        # })


