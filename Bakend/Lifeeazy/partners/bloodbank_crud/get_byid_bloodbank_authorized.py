from rest_framework import generics
from partners.serializer import BloodBankAuthorizedSerializer
from partners.models import BloodBankAuthorizedModel
from genericresponse import GenericResponse
from rest_framework.response import Response
from errormessage import Errormessage
import json

class GetByIdBloodBanksAuthorizedAPI(generics.GenericAPIView):
    serializer_class=BloodBankAuthorizedSerializer

    def get(self,request,id):
        try:
            result=BloodBankAuthorizedModel.objects.get(id=id)
            serializer_class=BloodBankAuthorizedSerializer(result)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = serializer_class.data
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
