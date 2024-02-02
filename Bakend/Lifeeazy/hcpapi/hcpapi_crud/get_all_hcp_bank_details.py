from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import AddbankdetailsSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import Addbankdetails




class get_all_hcp_bank_details(generics.GenericAPIView):
    serializer_class = AddbankdetailsSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = Addbankdetails.objects.all()
        serializer_class = AddbankdetailsSerializer(queryset, many=True)
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = serializer_class.data
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)