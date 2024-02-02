from rest_framework import generics
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import AddbankdetailsSerializer
from genericresponse import GenericResponse
import json


class HcpAddbankdetailsApi(generics.GenericAPIView):
    serializer_class = AddbankdetailsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = AddbankdetailsSerializer(user).data
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)