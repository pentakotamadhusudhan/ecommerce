from datetime import datetime
from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import AppointmentSerializer
from errormessage import Errormessage


class CreateUserAppointment(generics.GenericAPIView):
    serializer_class = AppointmentSerializer

    def post(self, request, *args, **kwargs):
        try:
            appointment = request.data.get('DoctorId')
            model1 = apps.get_model('hcpappointment', 'HcpScheduler')
            hcpAppoint = model1.objects.get(HcpId_id=appointment)
            fromdate = hcpAppoint.FromDate
            todate = hcpAppoint.ToDate
            fromtime = hcpAppoint.FromTIme
            totime = hcpAppoint.ToTime
            a_date = request.data.get('Date')
            a_time = request.data.get('Time')
            date1 = datetime.strptime(a_date, '%Y-%m-%d')
            time = datetime.strptime(a_time, '%H:%M:%S')
            time1 = datetime.time(time)
            date2 = datetime.date(date1)
            if fromdate <= date2 <= todate:
                if fromtime <= time1 <= totime:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    device_token = 'fkkrT-PGQn6t8FvXhR50NY:APA91bH7kxRHWmXOhX0nZcM6zqXamk0-wlqTj0-LGUZBWZ27jm_JnqUowMf5qO' \
                                   '-RTRAUBybAkiFhI2IkChPfq5NdA-q3O6mCDN-Q21HviTKgJaeUm0IQI78QGY_2XkLZGQj2ZD52YYeP '
                    title = "Appointment successful"
                    body = f"doctor will accept the your appointment at {date2} in {time1}"
                    FCMF_token(body, title, device_token)
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = AppointmentSerializer(user).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Please enter the current date and time"
                response.Result = False
                response.Status = 200
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)



