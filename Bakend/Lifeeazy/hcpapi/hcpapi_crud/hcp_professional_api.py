import json
from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpProfessionalSerializer
from genericresponse import GenericResponse
from errormessage import Errormessage


class HcpProfessionalApi(generics.GenericAPIView):
    serializer_class = HcpProfessionalSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'Message': 'Successful',
                'Result': HcpProfessionalSerializer(user).data,
                'HasError': False,
                'Status': 200})
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
