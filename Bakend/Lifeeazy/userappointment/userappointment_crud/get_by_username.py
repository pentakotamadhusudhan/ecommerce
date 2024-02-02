from datetime import datetime
from django.apps import apps
from rest_framework import viewsets, generics
from rest_framework.views import APIView, Response
from userappointment.serializers import AppointmentSerializer,Appointments,GetUserDetails
from userappointment.models import AppointmentModel
from firebase import FCMF_token
import json
from genericresponse import GenericResponse


class GetAppointmentByusername(generics.GenericAPIView):
    serializer_class = Appointments

    def get(self, request, Username):
        userModel = apps.get_model("user","UserModel")
        print(Username)
        user = userModel.objects.get(Username=Username)
        userid = user.id
        print(userid)
        result = AppointmentModel.objects.filter(UserId_id=userid)
        serializer_class = Appointments(result, many=True)
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
