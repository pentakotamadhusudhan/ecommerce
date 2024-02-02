from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.apps import apps
import json
from genericresponse import GenericResponse
from hcpprescription.serializers import GetPrescriptionData, GetPrescriptionSerializers
from errormessage import Errormessage


class HcpPresciptionById(generics.GenericAPIView):
    serializer_class = GetPrescriptionSerializers
    renderer_classes = [JSONRenderer]

    def get(self, request, HcpId):
        data = apps.get_model('hcpapi', 'HcpModel')
        try:
            model = data.objects.get(id=HcpId)
            serializer = GetPrescriptionData(model)
            return Response({'Message': 'Successfull',
                             'Result': serializer.data,
                             'HasError': True,
                             'Status': 500
                             })
        except data.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
