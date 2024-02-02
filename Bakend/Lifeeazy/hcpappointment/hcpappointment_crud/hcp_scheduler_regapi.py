from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from datetime import datetime
from django.apps import apps
from hcpappointment.serializers import HcpAppointSerializer
from errormessage import Errormessage
from hcpappointment.models import HcpScheduler
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class HcpSchedulerRegAPI(generics.GenericAPIView):
    serializer_class = HcpAppointSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # device_token = 'fkkrT-PGQn6t8FvXhR50NY:APA91bH7kxRHWmXOhX0nZcM6zqXamk0-wlqTj0-LGUZBWZ27jm_JnqUowMf5qO' \
            #                '-RTRAUBybAkiFhI2IkChPfq5NdA-q3O6mCDN-Q21HviTKgJaeUm0IQI78QGY_2XkLZGQj2ZD52YYeP '
            # title = "Appointment successful"
            # body = "doctor will accept the your appointment"
            # FCMF_token(body, title, device_token)
            user = serializer.save()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = HcpAppointSerializer(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)




