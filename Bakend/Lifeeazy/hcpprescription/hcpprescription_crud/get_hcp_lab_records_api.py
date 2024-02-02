from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from hcpprescription.serializers import GetLabrecordsSerializers, UserlabRecords
from errormessage import Errormessage


class GetHcpLabRecordsAPI(generics.GenericAPIView):
    serializer_class = GetLabrecordsSerializers
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = UserlabRecords.objects.all()
            serializer_class = GetLabrecordsSerializers(queryset, many=True)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except UserlabRecords.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

