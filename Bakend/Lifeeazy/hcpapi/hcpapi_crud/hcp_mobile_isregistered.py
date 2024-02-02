from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import HcpSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpModel
from errormessage import Errormessage


class HcpMobileIsRegistered(APIView):
    serializer_class = HcpSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, MobileNumber):
        if MobileNumber:
            try:
                res = HcpModel.objects.get(MobileNumber=MobileNumber)
                serializer = HcpSerializer(res)
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            except HcpModel.DoesNotExist as e:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = Errormessage(e)
                response.Result = []
                response.Status = 200
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
