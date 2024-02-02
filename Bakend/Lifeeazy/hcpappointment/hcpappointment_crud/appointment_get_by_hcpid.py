from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import HcpScheduler,HcpAppointSerializer
from errormessage import Errormessage


class AppointmentGetByHcpId(generics.GenericAPIView):
    serializer_class = HcpAppointSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, HcpId):
        try:
            data = HcpScheduler.objects.get(HcpId=HcpId)
            serializer_class = HcpAppointSerializer(data)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except HcpScheduler.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
