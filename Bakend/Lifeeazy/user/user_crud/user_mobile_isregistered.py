import json


from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import UserSerializer
from user.models import UserModel
from errormessage import Errormessage


class UserMobileIsRegisterd(APIView):
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, MobileNumber):
        if MobileNumber:
            try:
                res = UserModel.objects.get(MobileNumber=MobileNumber)
                output = UserSerializer(res).data
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = output
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            except UserModel.DoesNotExist as e:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = Errormessage(e)
                response.Result = False
                response.Status = 404
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=404)

