
from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from profileimage.serializers import ImageSerializer
from errormessage import Errormessage


class ImageUpload(generics.GenericAPIView):
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = GenericResponse("Message", "Result", "Status", "HasError")
        response.Message = "Successful"
        response.Result = ImageSerializer(user).data
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)


