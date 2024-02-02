from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from hcpappointment.serializers import DoctorStatus,UserStatus
from errormessage import Errormessage
from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class DoctorStatusUpdate(generics.GenericAPIView):
    serializer_class = DoctorStatus

    def put(self, request, id):
        try:
            MyModel1 = apps.get_model('userappointment', 'AppointmentModel')
            if MyModel1.objects.get(id=id):
                userappointment = MyModel1.objects.get(id=id)
                doctorId = userappointment.DoctorId_id
                print("doctorId" + " " + str(doctorId))
                userid = userappointment.UserId_id
                MyModel2 = apps.get_model('user', 'UserModel')
                appointment = MyModel2.objects.get(id=userid)
                email = appointment.Email
                Firstname = appointment.Firstname

                MyModel3 = apps.get_model('hcpapi', 'HcpModel')
                DoctorName = MyModel3.objects.get(id=userappointment.DoctorId_id)
                doctorname = DoctorName.Firstname + DoctorName.Lastname
                device_token = appointment.DeviceToken
                body = doctorname + " " + "doctor is accept your appointment"
                title = 'Appointment Confirmation'
                FCMF_token(body, title, device_token)
                userappointment.Status = request.data.get("Status")
                userappointment.save()


                if userappointment.Status =='CONFIRMED':
                    print("if")
                    Username = request.data.get('Username')
                    htmly = get_template('appointment_confirmed.html')
                    d = {'Username': Username,'Firstname':Firstname}
                    subject, from_email, to = 'Congrats Your Appointment is Confirmed', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                elif userappointment.Status =="CANCELLED":
                    print("elif")
                    Username = request.data.get('Username')
                    htmly = get_template('appointment_cancelled.html')
                    d = {'Username': Username,'Firstname':Firstname}
                    subject, from_email, to = 'Congrats Your Appointment is Cancelled', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                else:
                    Username = request.data.get('Username')
                    htmly = get_template('appointment_completed_with_next_followup_date.html')
                    d = {'Username': Username,'Firstname':Firstname}
                    subject, from_email, to = 'Congrats Your Appointment is Completed', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                serializer_class = UserStatus(userappointment)
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Successful"
                response.Result = serializer_class.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 404
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
