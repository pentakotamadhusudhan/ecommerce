from rest_framework import generics
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from hcpprescription.serializers import PrescriptionSerializers
from errormessage import Errormessage


class HcpPrescriptionRegAPI(generics.GenericAPIView):
    serializer_class = PrescriptionSerializers

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            user = serializer.save()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = PrescriptionSerializers(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

