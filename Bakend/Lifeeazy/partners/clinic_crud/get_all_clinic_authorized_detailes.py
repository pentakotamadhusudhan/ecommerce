import json
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from partners.serializer import AutherizedSerializer
from partners.models import AuthorizedModel
from errormessage import Errormessage


class GetAuthorizedList(APIView):
    serializer_class = AutherizedSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = AuthorizedModel.objects.all()
            serializer_class = AutherizedSerializer(queryset, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
