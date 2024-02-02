import json


from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import GetFamilyMember
from user.models import FamilyMember
from errormessage import Errormessage


class GetFamilyMembers(APIView):
    serializer_class = GetFamilyMember
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            result = FamilyMember.objects.all()
            prodata = GetFamilyMember(result, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = prodata.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
