from rest_framework import generics, permissions, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.apps import apps
import json
from genericresponse import GenericResponse
from hcpprescription.serializers import GetPrescriptionSerializersbyuser
from errormessage import Errormessage
from hcpprescription.models import UserPrescription


class HcpPresciptionByUserId(generics.GenericAPIView):
    serializer_class = GetPrescriptionSerializersbyuser
    renderer_classes = [JSONRenderer]

    def get(self, request, UserId):
        try:
            model = UserPrescription.objects.filter(UserId_id=UserId)
            serializer = GetPrescriptionSerializersbyuser(model,many=True)
            # response = GenericResponse("message", "result", "status", "has_error")
            # response.message = "Successful"
            # response.result = serializer.data
            # response.status = 200
            # response.has_error = False
            # jsonStr = json.dumps(response.__dict__)
            # return Response(json.loads(jsonStr), status=200)
            return Response({'Message': 'Successfull',
                             'Result': serializer.data,
                             'HasError': True,
                             'Status': 500
                             })
        except UserPrescription.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
