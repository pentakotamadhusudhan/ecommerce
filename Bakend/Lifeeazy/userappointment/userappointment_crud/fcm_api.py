from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import FCMSerializers
from firebase import FCMF_token
import json
from genericresponse import GenericResponse


class FCMApi(generics.GenericAPIView):
    serializer_class = FCMSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        title = request.data.get('title')
        body = request.data.get('body')
        device_token = request.data.get('device_token')
        user = FCMF_token(title, body, device_token)
        response = GenericResponse("message", "result", "status", "has_error")
        response.Message = "Successful"
        response.Result = user
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)
