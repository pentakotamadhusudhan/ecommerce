from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import UserStatus
from errormessage import Errormessage


class GetByDoctorName(generics.GenericAPIView):
    serializer_class = UserStatus

    def get(self, request, DoctorId):
        MyModel1 = apps.get_model('userappointment', 'AppointmentModel')
        data = MyModel1.objects.filter(DoctorId=DoctorId)
        serializer_class = UserStatus(data, many=True)
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
            response.Message = "Please enter the valid doctor id"
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
