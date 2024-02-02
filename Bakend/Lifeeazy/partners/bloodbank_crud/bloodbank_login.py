import json
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.models import BloodBankModel
from partners.serializer import LoginSerializerBloodBank,BloodBankSerializer


class BloodBankLoginview(generics.GenericAPIView):
    serializer_class = LoginSerializerBloodBank

    def post(self, request, format=None):
        username = request.data.get('RegisterUsername')
        password = request.data.get('RegisterPassword')
        if BloodBankModel.objects.filter(RegisterUsername=username).first():
            user = BloodBankModel.objects.filter(RegisterUsername=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializerBloodBank(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = BloodBankSerializer(user).data
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

        elif BloodBankModel.objects.filter(BloodBankEmailId=username).first():
            user = BloodBankModel.objects.filter(BloodBankEmailId=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializerBloodBank(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = BloodBankSerializer(user).data
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

        elif BloodBankModel.objects.filter(BloodBankContactNumber=username).first():
            user = BloodBankModel.objects.filter(BloodBankContactNumber=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = LoginSerializerBloodBank(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = BloodBankSerializer(user).data
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
        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "user not found"
            response.Result = []
            response.Status = 404
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
