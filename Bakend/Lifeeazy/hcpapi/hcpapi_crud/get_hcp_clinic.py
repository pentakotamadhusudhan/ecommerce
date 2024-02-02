from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from hcpapi.serializer import HcpClinicSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import Clinic


class GetHcpClinic(generics.GenericAPIView):
    serializer_class = HcpClinicSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
       # if Clinic.objects.all() == " ":
            queryset = Clinic.objects.all()
            serializer_class = HcpClinicSerializer(queryset, many=True)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Clinic has no data"
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
     
