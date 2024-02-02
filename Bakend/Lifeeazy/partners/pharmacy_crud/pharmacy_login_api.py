import json
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.models import PharmacyModel
from partners.serializer import PharmacyLoginSerializer, PharmacySerializer


class PharmacyLoginview(generics.GenericAPIView):
    serializer_class = PharmacyLoginSerializer

    def post(self, request, format=None):
        username = request.data.get('RegisterUsername')
        password = request.data.get('RegisterPassword')
        if PharmacyModel.objects.filter(RegisterUsername=username).first():
            user = PharmacyModel.objects.filter(RegisterUsername=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = PharmacyLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = PharmacySerializer(user).data
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

        elif PharmacyModel.objects.filter(PharmacyEmailId=username).first():
            user = PharmacyModel.objects.filter(PharmacyEmailId=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = PharmacyLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = PharmacySerializer(user).data
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

        elif PharmacyModel.objects.filter(PharmacyContactNumber=username).first():
            user = PharmacyModel.objects.filter(PharmacyContactNumber=username).first()
            if check_password(password, user.RegisterPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = PharmacyLoginSerializer(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                serializer_class = PharmacySerializer(user).data
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
