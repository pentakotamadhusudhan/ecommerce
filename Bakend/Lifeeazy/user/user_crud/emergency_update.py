import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import EmergencyUpdateSerializer
from user.models import UserEmergencyDetails
from errormessage import Errormessage


class EmergencyUpdate(generics.GenericAPIView):
    serializer_class = EmergencyUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserEmergencyDetails.objects.get(UserId=UserId)
            Person_Name = request.data.get("PersonName")
            RelationshipPatient = request.data.get("RelationshipPatient")
            PrimaryNumber = request.data.get("PrimaryNumber")
            MobileNumber = request.data.get("MobileNumber")
            Email = request.data.get("Email")
            data = {'Person_Name': Person_Name, 'RelationshipPatient': RelationshipPatient,
                    'PrimaryNumber': PrimaryNumber, 'MobileNumber': MobileNumber, 'Email': Email}
            s = EmergencyUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except UserEmergencyDetails.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Please enter the valid data to update"
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
