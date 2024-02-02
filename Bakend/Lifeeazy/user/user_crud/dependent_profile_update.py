import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import DependentProfileUpdateSerializer
from user.models import UserDependentProfile,UserProfile





class Dependent_ProfileUpdate(generics.GenericAPIView):
    serializer_class = DependentProfileUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserDependentProfile.objects.get(UserId=UserId)
            Title = request.data.get("Title")
            Gender = request.data.get("Gender")
            DOB = request.data.get("DOB")
            MartialStatus = request.data.get("MartialStatus")
            BloodGroup = request.data.get("BloodGroup")
            RelationshipToPatient = request.data.get("RelationshipToPatient")
            data = {'Title': Title, 'Gender': Gender, 'DOB': DOB, 'MartialStatus': MartialStatus,
                    'BloodGroup': BloodGroup, 'RelationshipToPatient': RelationshipToPatient}
            s = DependentProfileUpdateSerializer(r, data=data, partial=True)
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
        except UserProfile.DoesNotExist:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Not updated"
            response.Result = ""
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
            # return Response({'message': 'not updated',
            #                  'Result': False,
            #                  'HasError': True,
            #                  'status': 400
            #                  })
