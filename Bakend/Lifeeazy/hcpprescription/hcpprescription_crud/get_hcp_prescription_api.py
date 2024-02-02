from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json
from genericresponse import GenericResponse

from errormessage import Errormessage
from django.apps import apps
from hcpprescription.models import UserPrescription,UserlabRecords
from hcpprescription.serializers import AllPrescriptionDetails,Labdetails


class Data(generics.GenericAPIView):
    serializer_class=AllPrescriptionDetails

    def get(self, request):
        try:
            queryset = UserPrescription.objects.all()
            res=UserlabRecords.objects.all()
            serializer_class = AllPrescriptionDetails(queryset, many=True)
            output=Labdetails(res,many=True)
            result=serializer_class.data+output.data
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = result
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)

        except UserPrescription.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)



