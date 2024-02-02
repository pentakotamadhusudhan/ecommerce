from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import GetAppointment
from userappointment.models import AppointmentModel
import json
from genericresponse import GenericResponse
from errormessage import Errormessage


class GetAppointmentById(generics.GenericAPIView):
    serializer_class = GetAppointment

    def get(self, request, UserId):
        result = AppointmentModel.objects.filter(UserId_id=UserId)
        serializer_class = GetAppointment(result, many=True)
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
            response.Message = "AppointmentModel matching query does not exist."
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
