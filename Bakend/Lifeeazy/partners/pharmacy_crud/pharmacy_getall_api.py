from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from partners.serializer import PharmacySerializer
from genericresponse import GenericResponse
import json
from partners.models import PharmacyModel
from errormessage import Errormessage


class GetAllPharmacy(APIView):
    serializer_class = PharmacySerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = PharmacyModel.objects.all()
            serializer_class = PharmacySerializer(queryset, many=True)
            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})
        except Clinic.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
