import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import AddressUpdateSerializer
from user.models import UserAddress
from errormessage import Errormessage


class AddressUpdate(generics.GenericAPIView):
    serializer_class = AddressUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserAddress.objects.get(UserId=UserId)
            Address = request.data.get("Address")
            Country = request.data.get("Country")
            State = request.data.get("State")
            City = request.data.get("City")
            ZipCode = request.data.get("ZipCode")
            PrimaryNumber = request.data.get("PrimaryNumber")

            data = {'Address': Address, 'Country': Country, 'State': State, 'City': City, 'ZipCode': ZipCode,
                    'PrimaryNumber': PrimaryNumber}
            s = AddressUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except UserAddress.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Please enter the valid data to update"
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
