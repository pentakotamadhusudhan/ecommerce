from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import BillingSerializer
from userappointment.models import BillingModel
import json
from genericresponse import GenericResponse
from errormessage import Errormessage


class UserBillingView(generics.GenericAPIView):
    serializer_class = BillingSerializer

    def get(self, request, UserId, ):
        data = BillingModel.objects.filter(UserId_id=UserId)
        serializer_class = BillingSerializer(data, many=True)
        if serializer_class.data:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        else:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "BillingModel matching query does not exist."
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
