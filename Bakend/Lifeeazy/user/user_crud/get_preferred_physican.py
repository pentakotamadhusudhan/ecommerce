import json

from django.apps import apps
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, permissions, status, viewsets, authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from user.serializers import PhysicianSerializer
from user.models import Individualphysician


class GetPreferredPhysican(APIView):
    serializer_class = PhysicianSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, UserId):

        try:
            if UserId:
                res = Individualphysician.objects.filter(UserId=UserId)
                serializer_class = PhysicianSerializer(res, many=True)
                response1 = serializer_class.data
                # print(response)
                # new_dict = {k: v for elem in response for (k, v) in elem.items()}
                # new_dict = {k: v for k, v in response.items()}

                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = response1
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

        except Individualphysician.DoesNotExist:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "user does not exists"
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
            # return Response({'message': 'user does not exist',
            #                  'Result': False,
            #
            #                  'HasError': True,
            #                  'status': 400})
