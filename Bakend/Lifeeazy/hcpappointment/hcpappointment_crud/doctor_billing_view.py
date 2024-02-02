from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import DoctorBilling
from errormessage import Errormessage


class DoctorBillingView(generics.GenericAPIView):
    serializer_class = DoctorBilling

    def get(self, request, DoctorId):
        model = apps.get_model('userappointment', 'BillingModel')
        data = model.objects.filter(DoctorId=DoctorId)
        serializer_class = DoctorBilling(data, many=True)
        if serializer_class.data:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "BillingModel matching query does not exist."
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
