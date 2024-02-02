import json
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.models import UserModel
from user.serializers import LoginSerializer, UserSerializer


class Loginview(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if UserModel.objects.filter(Username=username).first():
            user = UserModel.objects.filter(Username=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = UserSerializer(user).data
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = serializer_class
                response.status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

            else:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        elif UserModel.objects.filter(Email=username).first():
            user = UserModel.objects.filter(Email=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = UserSerializer(user).data
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = serializer_class
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

            else:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        elif UserModel.objects.filter(MobileNumber=username).first():
            user = UserModel.objects.filter(MobileNumber=username).first()
            if check_password(password, user.Password):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = UserSerializer(user).data
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = serializer_class
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

            else:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "user not found"
                response.Result = []
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        response = GenericResponse("Message", "Result", "Status", "HasError")
        response.Message = "user not found"
        response.Result = []
        response.Status = 404
        response.HasError = True
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=400)
