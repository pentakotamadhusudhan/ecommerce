from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json
from django.apps import apps
from genericresponse import GenericResponse
from hcpprescription.serializers import GetLabrecordsSerializers,GetLabSerializers
from errormessage import Errormessage


class HcpLabRecordsById(generics.GenericAPIView):
    serializer_class = GetLabrecordsSerializers
    renderer_classes = [JSONRenderer]

    def get(self, request, HcpId):
        data = apps.get_model('hcpapi', 'HcpModel')
        try:
            model = data.objects.get(id=HcpId)
            serializer = GetLabSerializers(model)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except data.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)