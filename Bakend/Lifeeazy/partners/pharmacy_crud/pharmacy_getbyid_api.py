from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from partners.serializer import PharmacySerializer
from partners.models import PharmacyModel


class PharmacyGetById(generics.GenericAPIView):
    serializer_class = PharmacySerializer

    def get(self, request, id):
        if PharmacyModel.objects.filter(id=id):
            result = PharmacyModel.objects.filter(id=id)
            prodata = PharmacySerializer(result, many=True)
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
