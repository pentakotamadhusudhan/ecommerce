import json
from rest_framework import generics
from genericresponse import GenericResponse

from user.serializers import FamilyMemberAddressUpdateSerializer
from user.models import FamilyMemberAddress
from rest_framework.response import Response

from errormessage import Errormessage


class FamilyMemberAddressUpdateView(generics.GenericAPIView):
    serializer_class = FamilyMemberAddressUpdateSerializer

    def put(self, request, FamilyId):
        try:
            r = FamilyMemberAddress.objects.get(FamilyId=FamilyId)
            Address = request.data.get("Address")
            Country = request.data.get("Country")
            State = request.data.get("State")
            City = request.data.get("City")
            ZipCode = request.data.get("ZipCode")
            Primary_Number = request.data.get("Primary_Number")
            data = {'Address': Address, 'Country': Country, 'State': State, 'City': City, 'ZipCode': ZipCode,
                    'Primary_Number': Primary_Number}
            s = FamilyMemberAddressUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except FamilyMemberAddress.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

