import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import DependentAddressUpdateSerializer
from user.models import UserDependentAddress



class DependentAddressUpdate(generics.GenericAPIView):
    serializer_class = DependentAddressUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserDependentAddress.objects.get(UserId=UserId)
            Address = request.data.get("Address")
            Country = request.data.get("Country")
            State = request.data.get("State")
            City = request.data.get("City")
            ZipCode = request.data.get("ZipCode")
            Primary_Number = request.data.get("Primary_Number")
            data = {'Address': Address, 'Country': Country, 'State': State, 'City': City, 'ZipCode': ZipCode,
                    'Primary_Number': Primary_Number}
            s = DependentAddressUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
            # return Response({'message': ' Successful',
            #                  'Result': True,
            #                  'HasError': False,
            #                  'status': 200
            #                  })
        except UserDependentAddress.DoesNotExist:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Not updated"
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
            # return Response({'message': 'not updated',
            #                  'Result': False,
            #                  'HasError': True,
            #                  'status': 400
            #                  })

