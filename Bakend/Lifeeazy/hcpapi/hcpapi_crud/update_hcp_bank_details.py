from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import UpdatebankdetailsSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import Addbankdetails


class update_hcp_bank_details(generics.GenericAPIView):
    serializer_class = UpdatebankdetailsSerializer

    def put(self, request, id):
        try:
            r = Addbankdetails.objects.get(id=id)
            BankAccountNumber = request.data.get("BankAccountNumber")
            BankName = request.data.get("BankName")
            IFSCCode = request.data.get("IFSCCode")
            BankBranch = request.data.get("BankBranch")
            AccountNumber = request.data.get("AccountNumber")
            PanNumber = request.data.get("PanNumber")
            UploadPancard = request.data.get("UploadPancard")
            UploadDocuments = request.data.get("UploadDocuments")
            Remarks = request.data.get("Remarks")
            data = {'BankAccountNumber': BankAccountNumber, 'BankName': BankName, 'IFSCCode': IFSCCode,
                    'BankBranch': BankBranch, 'AccountNumber': AccountNumber, 'PanNumber': PanNumber,
                    'UploadPancard': UploadPancard, 'UploadDocuments': UploadDocuments, 'Remarks': Remarks}
            s = UpdatebankdetailsSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
            # return Response({'message': 'Successful',
            #                  'Result': True,
            #                  'HasError': False,
            #                  'status': 200
            #                  })
        except Addbankdetails.DoesNotExist:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Please enter the valid data"
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
            # return Response({'message': 'Please enter the valid data',
            #                  'Result': False,
            #                  'HasError': True,
            #                  'status': 500
            #                  })
