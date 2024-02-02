<<<<<<< HEAD
from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import RegSerializer, LoginSerializer, AddressSerializer, EmergencySerializer, UserSerializer, \
    ChangePasswordSerializerAPI, ProfileSerializer, ProfileUpdateSerializer, DependentProfileSerializer, \
    DependentEmergencyDetailSerializer, DependentAddressSerializer, DependentProfileUpdateSerializer, \
    AddressUpdateSerializer, EmergencyUpdateSerializer, DependentAddressUpdateSerializer, \
    DependentEmergencyDetailsUpdateSerializer, HcpSerializer, FCMSerializers,PhysicianSerializer,PreferredSerializer,PhysicianSerializerGet

class Dependent_EmergencyView(generics.GenericAPIView):
    serializer_class = DependentEmergencyDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = DependentEmergencyDetailSerializer(user).data
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)
=======
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.utils import json
# from genericresponse import GenericResponse
# from user.serializers import DependentEmergencyDetailSerializer
#
#
# class Dependent_EmergencyView(generics.GenericAPIView):
#     serializer_class = DependentEmergencyDetailSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         response = GenericResponse("Message", "Result", "Status", "HasError")
#         response.Message = "Successful"
#         response.Result = DependentEmergencyDetailSerializer(user).data
#         response.Status = 200
#         response.HasError = False
#         jsonStr = json.dumps(response.__dict__)
#         return Response(json.loads(jsonStr), status=200)
>>>>>>> 091857d69f4068f0ae7e2a6fdc03a7c56e5c7d5a
