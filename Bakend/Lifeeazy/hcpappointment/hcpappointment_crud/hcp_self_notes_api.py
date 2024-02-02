import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from hcpappointment.serializers import HcpSelfNoteSerializer, HcpUpdateSelfNoteSerializer
#from errormessage import Errormessage
from hcpappointment.models import HcpSelfNote

class HcpSelfNoteApi(generics.GenericAPIView):
    serializer_class = HcpSelfNoteSerializer

    def post(self,request,*args, **kwargs):
        try:
            HcpId=request.data.get("HcpId")
            AppointmentId=request.data.get("AppointmentId")
            model = HcpSelfNote.objects.filter(AppointmentId_id=AppointmentId)
            physicianData = int(HcpId)
            data = []
            for i in model:
                data.append(int(i.id))
            if HcpSelfNote.objects.filter(HcpId_id=HcpId,AppointmentId_id=AppointmentId).first():
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "doctor and appointmentid already exists"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
            elif physicianData not in data:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = HcpSelfNoteSerializer(user).data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Doctor is not related to the appointment id given"
            response.Result = []
            response.Status = 404
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=404)

