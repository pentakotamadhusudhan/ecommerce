from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from hcpapi.serializer import HcpClinicSerializer
import json
from hcpapi.models import Clinic


class GetClinicByID(generics.GenericAPIView):
    serializer_class = HcpClinicSerializer

    def get(self, request, HcpId):
        result = Clinic.objects.filter(HcpId=HcpId)
        serializer_class = HcpClinicSerializer(result, many=True)
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
            response.Message = "Clinic matching query does not exist"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
