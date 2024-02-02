from datetime import datetime

from django.apps import apps
from rest_framework import viewsets, generics
from rest_framework.views import APIView, Response

from userappointment.serializers import Prescriptionsserializer
#from userappointment.models import AppointmentModel
from firebase import FCMF_token
import json
from genericresponse import GenericResponse


class GetAppointmentByUserIdByHCPIdPrescriptionDetails(generics.GenericAPIView):
    serializer_class = Prescriptionsserializer

    def get(self, request, UserId,HcpId):
        MyModel1 = apps.get_model('hcpprescription','UserPrescription')
        result = MyModel1.objects.filter(UserId_id=UserId,HcpId_id=HcpId)
        serializer_class = Prescriptionsserializer(result, many=True)

        if serializer_class.data:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
            # return Response({'message': 'Successful',
            #                  'Result': serializer_class.data,
            #                  'HasError': False,
            #                  'status': 200})
        else:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "user not found"
            response.Result = []
            response.Status = 404
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
