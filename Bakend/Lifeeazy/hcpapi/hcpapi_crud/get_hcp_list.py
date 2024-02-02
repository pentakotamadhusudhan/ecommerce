from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import HcpRegSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpModel
from errormessage import Errormessage


class GetHcpList(APIView):
    serializer_class = HcpRegSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = HcpModel.objects.all()
            serializer_class = HcpRegSerializer(queryset, many=True)
            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

