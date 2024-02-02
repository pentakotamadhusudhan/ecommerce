import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from hcpappointment.serializers import HcpSelfNoteSerializer, HcpUpdateSelfNoteSerializer
from hcpappointment.models import HcpSelfNote

from errormessage import Errormessage


class SelfNoteUpdate(generics.GenericAPIView):
    serializer_class = HcpUpdateSelfNoteSerializer

    def put(self, request, id):
        try:
            r = HcpSelfNote.objects.get(id=id)
            HcpId = request.data.get("HcpId")
            AppointmentId = request.data.get("AppointmentId")
            UpdatedDate = request.data.get("UpdatedDate")
            SelfNote = request.data.get("SelfNote")
            data = {'HcpId': HcpId, 'AppointmentId': AppointmentId, 'UpdatedDate': UpdatedDate, 'SelfNote': SelfNote,
                    }
            s = HcpUpdateSelfNoteSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            return Response({'Message': ' Successful',
                             'Result': True,
                             'HasError': False,
                             'Status': 200
                             })
        except HcpSelfNote.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
