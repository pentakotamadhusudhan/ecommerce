import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import BloodBankAuthorizedUpdateSerializer
from partners.models import BloodBankAuthorizedModel
from errormessage import Errormessage
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.hashers import make_password

class BloodbankAuthorizedUpdateView(generics.GenericAPIView):
    serializer_class = BloodBankAuthorizedUpdateSerializer

    def put(self, request, id):
        try:
            r = BloodBankAuthorizedModel.objects.get(id=id)
            BloodBankId = request.data.get("BloodBankId")
            FirstName = request.data.get("FirstName")
            LastName = request.data.get("LastName")
            EmailId = request.data.get("EmailId")
            MobileNumber = request.data.get("MobileNumber")
            data = {'BloodBankId': BloodBankId,
                    'FirstName': FirstName,
                    'LastName':LastName,
                    'EmailId': EmailId,
                    'MobileNumber': MobileNumber
                    }
            s = BloodBankAuthorizedUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except BloodBankModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
