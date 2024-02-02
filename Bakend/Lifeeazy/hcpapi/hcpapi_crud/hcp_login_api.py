from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpLoginSerializer,HcpSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpModel


class HcpLoginAPI(generics.GenericAPIView):
    serializer_class = HcpLoginSerializer

    def post(self, request, format=None):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if HcpModel.objects.filter(Username=username).first():
            user = HcpModel.objects.filter(Username=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = HcpLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = HcpSerializer(user).data
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class
                response.Status = 200
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=404)
        elif HcpModel.objects.filter(Email=username).first():
            user = HcpModel.objects.filter(Email=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = HcpLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = HcpSerializer(user).data
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=404)
        elif HcpModel.objects.filter(MobileNumber=username).first():
            user = HcpModel.objects.filter(MobileNumber=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = HcpLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = HcpSerializer(user).data
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=404)
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "please enter valid details"
        response.Result = []
        response.Status = 400
        response.HasError = True
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=400)
