from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import GetAppointment
import json
from genericresponse import GenericResponse
from userappointment.models import AppointmentModel
from errormessage import Errormessage


class GetAppointments(generics.GenericAPIView):
    serializer_class = GetAppointment

    def get(self, request):
        try:
            result = AppointmentModel.objects.all()
            serializer_class = GetAppointment(result, many=True)

            if serializer_class.data:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
