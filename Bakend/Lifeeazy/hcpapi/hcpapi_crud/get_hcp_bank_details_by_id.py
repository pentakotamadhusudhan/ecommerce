from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import AddbankdetailsSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import Addbankdetails


class get_hcp_bank_details_by_id(APIView):
    serializer_class = AddbankdetailsSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, HcpId):
        data = Addbankdetails.objects.get(HcpId=HcpId)
        serializer_class = AddbankdetailsSerializer(data)
        return Response({'Message': 'Successful',
                         'Result': serializer_class.data,
                         'HasError': False,
                         'Status': 200})
