from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import FCMSerializers
from genericresponse import GenericResponse
import json
from firebase import FCMF_token


class FCMApi(generics.GenericAPIView):
    serializer_class = FCMSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        title = request.data.get('title')
        body = request.data.get('body')
        DeviceToken = request.data.get('DeviceToken')

        user = FCMF_token(title, body, DeviceToken)
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = user
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)
