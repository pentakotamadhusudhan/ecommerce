from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import FCMSerializers


class FCMApi(generics.GenericAPIView):
    serializer_class = FCMSerializers

    def post(self, request, *args, **kwargs):
        serializer = FCMSerializers(data=request.data)
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
