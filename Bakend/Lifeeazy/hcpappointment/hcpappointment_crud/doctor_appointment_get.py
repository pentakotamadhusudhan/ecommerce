from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import HcpAppointSerializer, HcpScheduler
from errormessage import Errormessage


class DoctorAppointmentGet(generics.GenericAPIView):
    serializer_class = HcpAppointSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = HcpScheduler.objects.all()
            serializer_class = HcpAppointSerializer(queryset, many=True)
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
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
