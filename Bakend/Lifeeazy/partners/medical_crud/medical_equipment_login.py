import json
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.models import MedicalEquipmentModel
from partners.serializer import MedicalLoginSerializer, MedicalEquipmentSerializer


class MedicalLoginApi(generics.GenericAPIView):
    serializer_class = MedicalLoginSerializer

    def post(self, request, format=None):
        username = request.data.get('RegisteredUsername')
        password = request.data.get('RegisteredPassword')
        if MedicalEquipmentModel.objects.filter(RegisteredUsername=username).first():
            user = MedicalEquipmentModel.objects.filter(RegisteredUsername=username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = MedicalLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = MedicalEquipmentSerializer(user).data
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

        elif MedicalEquipmentModel.objects.filter(ProviderEmailId=username).first():
            user = MedicalEquipmentModel.objects.filter(ProviderEmailId=username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = MedicalLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = MedicalEquipmentSerializer(user).data
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

        elif MedicalEquipmentModel.objects.filter(ProviderContact=username).first():
            user = MedicalEquipmentModel.objects.filter(ProviderContact=username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = MedicalLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = MedicalEquipmentSerializer(user).data
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
