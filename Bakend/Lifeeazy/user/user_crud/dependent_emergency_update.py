<<<<<<< HEAD
import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import DependentEmergencyDetailsUpdateSerializer
from user.models import UserDependentEmergencyDetails



class DependentEmergencyUpdate(generics.GenericAPIView):
    serializer_class = DependentEmergencyDetailsUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserDependentEmergencyDetails.objects.get(UserId=UserId)
            Person_Name = request.data.get("PersonName")
            Relationship_Patient = request.data.get("RelationshipPatient")
            Primary_Number = request.data.get("PrimaryNumber")
            Mobile_Number = request.data.get("MobileNumber")
            Email = request.data.get("Email")

            data = {'PersonName': Person_Name, 'RelationshipPatient': Relationship_Patient,
                    'PrimaryNumber': Primary_Number, 'MobileNumber': Mobile_Number, 'Email': Email}

            s = DependentEmergencyDetailsUpdateSerializer(r, data=data, partial=True)
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
        except UserDependentEmergencyDetails.DoesNotExist:
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

=======
# import json
# from rest_framework import generics
# from rest_framework.response import Response
# from genericresponse import GenericResponse
# from user.serializers import DependentEmergencyDetailsUpdateSerializer
# from user.models import UserDependentEmergencyDetails
#
#
# class DependentEmergencyUpdate(generics.GenericAPIView):
#     serializer_class = DependentEmergencyDetailsUpdateSerializer
#
#     def put(self, request, UserId):
#         try:
#             r = UserDependentEmergencyDetails.objects.get(UserId=UserId)
#             Person_Name = request.data.get("PersonName")
#             Relationship_Patient = request.data.get("RelationshipPatient")
#             Primary_Number = request.data.get("PrimaryNumber")
#             Mobile_Number = request.data.get("MobileNumber")
#             Email = request.data.get("Email")
#
#             data = {'PersonName': Person_Name, 'RelationshipPatient': Relationship_Patient,
#                     'PrimaryNumber': Primary_Number, 'MobileNumber': Mobile_Number, 'Email': Email}
#
#             s = DependentEmergencyDetailsUpdateSerializer(r, data=data, partial=True)
#             s.is_valid(raise_exception=True)
#             s.save()
#             response = GenericResponse("Message", "Result", "Status", "HasError")
#             response.Message = "Successful"
#             response.Result = True
#             response.Status = 200
#             response.HasError = False
#             jsonStr = json.dumps(response.__dict__)
#             return Response(json.loads(jsonStr), status=200)
#         except UserDependentEmergencyDetails.DoesNotExist:
#             response = GenericResponse("Message", "Result", "Status", "HasError")
#             response.Message = "data not update"
#             response.Result = ""
#             response.Status = 400
#             response.HasError = True
#             jsonStr = json.dumps(response.__dict__)
#             return Response(json.loads(jsonStr), status=400)
#
>>>>>>> 091857d69f4068f0ae7e2a6fdc03a7c56e5c7d5a
