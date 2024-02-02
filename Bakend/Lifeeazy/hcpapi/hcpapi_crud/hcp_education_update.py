from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpEducationUpdateSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpEducational
from errormessage import Errormessage


class HcpEducationUpdate(generics.GenericAPIView):
    serializer_class = HcpEducationUpdateSerializer

    def put(self, request, HcpId):
        try:
            r = HcpEducational.objects.get(HcpId=HcpId)
            Degree = request.data.get("Degree")
            CollegeUniversity = request.data.get("CollegeUniversity")
            Year = request.data.get("YearOfEducation")
            EducationalLocation = request.data.get("EducationalLocation")
            data = {'Degree': Degree, 'CollegeUniversity': CollegeUniversity, 'YearOfEducation': Year,
                    'EducationalLocation': EducationalLocation}
            s = HcpEducationUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except HcpEducational.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)

