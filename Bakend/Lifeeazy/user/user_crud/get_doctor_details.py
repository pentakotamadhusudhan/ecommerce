import json
from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import HcpSerializer
from errormessage import Errormessage


class GetDoctorDetails(generics.GenericAPIView):
    serializer_class = HcpSerializer

    def get(self, request):
        try:
            MyModel1 = apps.get_model('hcpapi', 'HcpModel')
            data = MyModel1.objects.all()
            serializer_class = HcpSerializer(data, many=True)
            if serializer_class.data:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = serializer_class.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
