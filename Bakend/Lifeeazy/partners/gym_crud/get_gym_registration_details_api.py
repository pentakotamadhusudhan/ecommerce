from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from partners.serializer import GymRegistrationSerializer
from genericresponse import GenericResponse
import json
from partners.models import GymModel
from errormessage import Errormessage

class GetAllGymRegistredDetailsApi(APIView):
    serializer_class = GymRegistrationSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = GymModel.objects.all()
            serializer_class = GymRegistrationSerializer(queryset, many=True)
            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})
        except GymModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
