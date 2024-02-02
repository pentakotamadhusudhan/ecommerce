from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpProfessionalUpdateSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpProfessional
from errormessage import Errormessage


class HcpProfessionalUpdate(generics.GenericAPIView):
    serializer_class = HcpProfessionalUpdateSerializer

    def put(self, request, HcpId):
        try:
            r = HcpProfessional.objects.get(HcpId=HcpId)
            ProfessionalId = request.data.get("ProfessionalId")
            ProfessionalExperienceInYears = request.data.get("ProfessionalExperienceInYears")
            CurrentStatus = request.data.get("CurrentStatus")
            MciNumber = request.data.get("MciNumber")
            MciStateCouncil = request.data.get("MciStateCouncil")
            Specialization = request.data.get("Specialization")
            AreaFocusOn = request.data.get("AreaFocusOn")
            PatientsHandledPerDay = request.data.get("PatientsHandledPerDay")
            PatientsHandledPerSlot = request.data.get("PatientsHandledPerSlot")
            AppointmentType = request.data.get("AppointmentType")
            Signature = request.data.get('Signature')

            data = {'ProfessionalId': ProfessionalId,
                    'ProfessionalExperienceInYears': ProfessionalExperienceInYears,
                    'CurrentStatus': CurrentStatus, 'MciNumber': MciNumber, 'MciStateCouncil': MciStateCouncil,
                    'Specialization': Specialization, 'AreaFocusOn': AreaFocusOn,
                    'PatientsHandledPerDay': PatientsHandledPerDay,
                    'PatientsHandledPerSlot': PatientsHandledPerSlot, 'AppointmentType': AppointmentType,
                    'Signature': Signature}
            s = HcpProfessionalUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            return Response({'Message': 'Successful',
                             'Result': s.data,
                             'HasError': False,
                             'Status': 200})
        except HcpProfessional.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
