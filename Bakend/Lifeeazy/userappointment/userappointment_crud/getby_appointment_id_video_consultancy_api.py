from rest_framework import generics
from rest_framework.views import Response
from userappointment.serializers import VideoConsultSerializer
from userappointment.models import VideoConsultModel
import json
from genericresponse import GenericResponse
from errormessage import Errormessage
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class GetByAppointmentIdVideoConsult(APIView):
    serializer_class = VideoConsultSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, AppointmentId):
        result = VideoConsultModel.objects.filter(AppointmentId=AppointmentId)
        serializer_class = VideoConsultSerializer(result, many=True)
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
            response.Message = "AppointmentModel matching query does not exist."
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
