from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import AppointmentSerializer
from userappointment.models import AppointmentModel
import json
from genericresponse import GenericResponse
from errormessage import Errormessage


class ByStatus(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get(self, request, Status):
        result = AppointmentModel.objects.filter(Status=Status)
        serializer_class = AppointmentSerializer(result, many=True)
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
