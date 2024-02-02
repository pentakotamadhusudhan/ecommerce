from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from partners.serializer import ClinicProfileSerializer
from genericresponse import GenericResponse
import json
from partners.models import ClinicProfile




class ClinicProfileGetById(generics.GenericAPIView):
    serializer_class = ClinicProfileSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request,ClinicId):
        queryset = ClinicProfile.objects.filter(ClinicId=ClinicId)
        serializer_class = ClinicProfileSerializer(queryset, many=True)
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = serializer_class.data
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)