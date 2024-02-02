from rest_framework import generics
from partners.serializer import BloodBankSerializer
from partners.models import BloodBankModel
from genericresponse import GenericResponse
from rest_framework.response import Response
from errormessage import Errormessage
import json

class GetBloodBanksById(generics.GenericAPIView):
    serializer_class=BloodBankSerializer

    def get(self,request,id):
        try:
            result=BloodBankModel.objects.get(id=id)
            output=BloodBankSerializer(result)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = output.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
