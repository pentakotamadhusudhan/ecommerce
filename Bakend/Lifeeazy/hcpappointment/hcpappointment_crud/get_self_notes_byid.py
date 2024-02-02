import json
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from hcpappointment.serializers import HcpSelfNoteSerializer, HcpUpdateSelfNoteSerializer
from hcpappointment.models import HcpSelfNote
from errormessage import Errormessage


class GetSelfNotes(APIView):
    serializer_class = HcpSelfNoteSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, id):
        try:
            data = HcpSelfNote.objects.get(id=id)
            serializer_class = HcpSelfNoteSerializer(data)
            return Response({
                'Message': 'Successful',
                'Result': serializer_class.data,
                'HasError': False,
                'Status': 200

            })
        except HcpSelfNote.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 404
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
