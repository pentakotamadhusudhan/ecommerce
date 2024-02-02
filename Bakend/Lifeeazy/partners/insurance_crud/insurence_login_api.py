from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import InsuranceLoginSerializers
from genericresponse import GenericResponse
import json
from partners.models import InsuranceRegistrationModel


class InsuranceLoginAPI(generics.GenericAPIView):
    serializer_class = InsuranceLoginSerializers

    def post(self,request,format=None):
        username = request.data.get('RegisteredUsername')
        password = request.data.get('RegisteredPassword')
        if InsuranceRegistrationModel.objects.filter(RegisteredUsername=username).first():
            user = InsuranceRegistrationModel.objects.filter(RegisteredUsername=username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken': DeviceToken}
                    s = InsurenceLoginSerializers(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = s.data
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
        elif InsuranceRegistrationModel.objects.filter(InsuranceCompanyEmailId = username).first():
            user = InsuranceRegistrationModel.objects.filter(InsuranceCompanyEmailId = username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken':DeviceToken}
                    s = InsurenceLoginSerializers(user, data=data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = s.data
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
        elif InsuranceRegistrationModel.objects.filter(InsuranceCompanyContact = username).first():
            user = InsuranceRegistrationModel.objects.filter(InsuranceCompanyContact = username).first()
            if check_password(password, user.RegisteredPassword):
                if request.data.get('DeviceToken') == "":
                    user.DeviceToken = user.DeviceToken
                    user.save()
                else:
                    DeviceToken = request.data.get("DeviceToken")
                    data = {'DeviceToken':DeviceToken}
                    s  = InsurenceLoginSerializers(user, data = data, partial=True)
                    s.is_valid(raise_exception=True)
                    s.save()
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = s.data
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











