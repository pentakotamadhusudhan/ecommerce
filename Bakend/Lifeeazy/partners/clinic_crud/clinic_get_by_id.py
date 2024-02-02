from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from partners.serializer import ClinicSerializer
from partners.models import Clinic


class ClinicGetById(generics.GenericAPIView):
    serializer_class = ClinicSerializer

    def get(self, request, id):
        if Clinic.objects.filter(id=id):
            result = Clinic.objects.filter(id=id)
            prodata = ClinicSerializer(result, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = prodata.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Clinic matching query does not exist"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
