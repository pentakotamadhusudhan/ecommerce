from rest_framework import generics
from rest_framework.response import Response
from firebase import FCMF_token
from genericresponse import GenericResponse
import json
from datetime import datetime
from django.apps import apps
from userappointment.serializers import NewAppointmentSerializer, AppointmentSerializer
from userappointment.models import AppointmentModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from user .models import UserModel


class CreateUserAppointment(generics.GenericAPIView):
    serializer_class = NewAppointmentSerializer

    def post(self, request):
        try:
            doctorId = request.data.get('DoctorId')
            schedule = request.data.get('ScheduleId')
            user_id = request.data.get('UserId')
            appointmentType = request.data.get('AppointmentType')
            family_id = request.data.get('FamilyMemberId')
            familyData = apps.get_model('user', 'FamilyMember')
            fees = request.data.get('Fees')
            family = familyData.objects.filter(UserId_id=user_id)
            FamilyMembers = []
            for i in family:
                FamilyMembers.append(int(i.id))

            model1 = apps.get_model('hcpappointment', 'HcpScheduler')
            hcpAppoint = model1.objects.get(id=schedule)
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
            appointtype = hcpAppoint.AppointmentType
            telefee = hcpAppoint.TeleconsultationFees
            inclincfee = hcpAppoint.InclinicFees
            homefee = hcpAppoint.HomeFees

            if family_id is None:
                if fromdate <= date2 <= todate:
                    #if fromtime <= time1 <= totime:
                        if appointmentType == appointtype:
                            if appointmentType == "Home" and fees == homefee:
                                UserData = {"UserId": request.data.get('UserId'),
                                            "DoctorId": request.data.get('DoctorId'),
                                            "ScheduleId": request.data.get('ScheduleId'),
                                            "FamilyMemberAge": request.data.get('FamilyMemberAge'),
                                            "FamilyMemberGender": request.data.get('FamilyMemberGender'),
                                            "FamilyMemberId": request.data.get('FamilyMemberId'),
                                            "Date": request.data.get('Date'),
                                            "AppointmentType": request.data.get('AppointmentType'),
                                            "Fees": homefee,
                                            "Time": request.data.get('Time'),
                                            "Specialization": request.data.get('Specialization'),
                                            "Status": request.data.get('Status'),
                                            "PrescriptionId":request.data.get('PrescriptionId')}
                                serializer = self.get_serializer(data=UserData)
                                serializer.is_valid(raise_exception=True)
                                user = serializer.save()
                                mymodel1 = apps.get_model('user', 'UserModel')
                                data = mymodel1.objects.get(id=user_id)
                                MyModel2 = apps.get_model('hcpapi', 'HcpModel')
                                DoctorName = MyModel2.objects.get(id=doctorId)
                                doctor = DoctorName.Firstname + DoctorName.Lastname
                                device_token = data.DeviceToken
                                title = "Appointment successful"
                                body = f"You will create a appointment at {a_date} in {a_time} and the doctor name is {doctor}"
                                FCMF_token(body, title, device_token)
                                return Response({
                                    'message': 'Successful',
                                    'Result': NewAppointmentSerializer(user).data,
                                    'HasError': False,
                                    'status': 200

                                })
                            elif appointmentType == "Inclinic" and  fees == inclincfee:
                                UserData = {"UserId": request.data.get('UserId'),
                                            "DoctorId": request.data.get('DoctorId'),
                                            "ScheduleId": request.data.get('ScheduleId'),
                                            "FamilyMemberAge": request.data.get('FamilyMemberAge'),
                                            "FamilyMemberGender": request.data.get('FamilyMemberGender'),
                                            "FamilyMemberId": request.data.get('FamilyMemberId'),
                                            "Date": request.data.get('Date'),
                                            "AppointmentType": request.data.get('AppointmentType'),
                                            "Fees": inclincfee,
                                            "Time": request.data.get('Time'),
                                            "Specialization": request.data.get('Specialization'),
                                            "Status": request.data.get('Status'),
                                            "PrescriptionId":request.data.get('PrescriptionId')}
                                serializer = self.get_serializer(data=UserData)
                                serializer.is_valid(raise_exception=True)
                                user = serializer.save()
                                mymodel1 = apps.get_model('user', 'UserModel')
                                data = mymodel1.objects.get(id=user_id)
                                MyModel2 = apps.get_model(
                                    'hcpapi',
                                    'HcpModel')
                                DoctorName = MyModel2.objects.get(id=doctorId)
                                doctor = DoctorName.Firstname + DoctorName.Lastname
                                device_token = data.DeviceToken
                                title = "Appointment successful"
                                body = f"You will create a appointment at {a_date} in {a_time} and the doctor name is {doctor}"
                                FCMF_token(body, title, device_token)
                                return Response({
                                    'message': 'Successful',
                                    'Result': NewAppointmentSerializer(user).data,
                                    'HasError': False,
                                    'status': 200

                                })

                            elif appointmentType == "Teleconsultation" and  fees == telefee:
                                UserData = {"UserId": request.data.get('UserId'),
                                            "DoctorId": request.data.get('DoctorId'),
                                            "ScheduleId": request.data.get('ScheduleId'),
                                            "FamilyMemberAge": request.data.get('FamilyMemberAge'),
                                            "FamilyMemberGender": request.data.get('FamilyMemberGender'),
                                            "FamilyMemberId": request.data.get('FamilyMemberId'),
                                            "Date": request.data.get('Date'),
                                            "AppointmentType": request.data.get('AppointmentType'),
                                            "Fees": telefee,
                                            "Time": request.data.get('Time'),
                                            "Specialization": request.data.get('Specialization'),
                                            "Status": request.data.get('Status'),
                                            "PrescriptionId":request.data.get('PrescriptionId')}
                                serializer = self.get_serializer(data=UserData)
                                serializer.is_valid(raise_exception=True)
                                user = serializer.save()
                                mymodel1 = apps.get_model('user', 'UserModel')
                                data = mymodel1.objects.get(id=user_id)
                                MyModel2 = apps.get_model('hcpapi', 'HcpModel')
                                DoctorName = MyModel2.objects.get(id=doctorId)
                                doctor = DoctorName.Firstname + DoctorName.Lastname
                                device_token = data.DeviceToken
                                title = "Appointment successful"
                                body = f"You will create a appointment at {a_date} in {a_time} and the doctor name is {doctor}"
                                FCMF_token(body, title, device_token)
                                return Response({
                                    'message': 'Successful',
                                    'Result': NewAppointmentSerializer(user).data,
                                    'HasError': False,
                                    'status': 200

                                })
                            else:
                                response = GenericResponse("Message", "Result", "Status", "HasError")
                                response.Message = "you have entered wrong fees"
                                response.Result = False
                                response.Status = 400
                                response.HasError = True
                                jsonStr = json.dumps(response.__dict__)
                                return Response(json.loads(jsonStr), status=400)
                        else:
                            response = GenericResponse("Message", "Result", "Status", "HasError")
                            response.Message = "you have entered wrong appointment type "
                            response.Result = False
                            response.Status = 400
                            response.HasError = True
                            jsonStr = json.dumps(response.__dict__)
                            return Response(json.loads(jsonStr), status=400)

                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "please select the valid date and time"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
            elif int(family_id) in FamilyMembers:
                family_data = familyData.objects.get(id=family_id)
                if family_data.FamilyMemberType == 'ADULT':
                    if fromdate <= date2 <= todate:
                        #if fromtime <= time1 <= totime:
                            try:
                                serializer = self.get_serializer(data=request.data)
                                serializer.is_valid(raise_exception=True)
                                user = serializer.save()

                                emailData = familyData.objects.get(id=family_id)

                                email = emailData.Email
                                Username = request.data.get('Username')

                                htmly = get_template('appointment_booking_notification.html')
                                d = {'Username': Username}
                                subject, from_email, to = 'Confirmation mail for appointment booked successfully for familymember', settings.FROM_EMAIL, email
                                html_content = htmly.render(d)
                                msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                                msg.attach_alternative(html_content, "text/html")
                                msg.send()

                                mymodel1 = apps.get_model('user', 'UserModel')
                                data = mymodel1.objects.get(id=user_id)
                                MyModel2 = apps.get_model('hcpapi', 'HcpModel')
                                DoctorName = MyModel2.objects.get(id=doctorId)
                                doctor = DoctorName.Firstname + DoctorName.Lastname
                                device_token = data.DeviceToken
                                title = "Appointment successful"
                                body = f"You will create the your appointment at {a_date} in {a_time} to the doctor {doctor} from family member Adult"
                                FCMF_token(body, title, device_token)
                                return Response({
                                    'message': 'Successful',
                                    'Result': NewAppointmentSerializer(user).data,
                                    'HasError': False,
                                    'status': 200

                                })
                            except Exception as e:
                                return Response({
                                    'message': 'Successful',
                                    'Result': Errormessage(e),
                                    'HasError': False,
                                    'status': 400

                                })
                    else:
                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "please select the valid date and time"
                        response.Result = False
                        response.Status = 400
                        response.HasError = True
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=400)
                elif family_data.FamilyMemberType == 'CHILD':
                    if fromdate < date2 < todate:
                        #if fromtime < time1 < totime:
                            serializer = self.get_serializer(data=request.data)
                            serializer.is_valid(raise_exception=True)
                            user = serializer.save()
                            mymodel1 = apps.get_model('user', 'UserModel')
                            data = mymodel1.objects.get(id=user_id)
                            MyModel2 = apps.get_model('hcpapi', 'HcpModel')
                            DoctorName = MyModel2.objects.get(id=doctorId)
                            doctor = DoctorName.Firstname + DoctorName.Lastname
                            device_token = data.DeviceToken
                            title = "Appointment successful"
                            body = f"You will create the your appointment at {a_date} in {a_time} to the doctor {doctor} from family member Child"
                            FCMF_token(body, title, device_token)
                            response = GenericResponse("Message", "Result", "Status", "HasError")
                            response.Message = "Successful"
                            response.Result = NewAppointmentSerializer(user).data
                            response.Status = 200
                            response.HasError = False
                            jsonStr = json.dumps(response.__dict__)
                            return Response(json.loads(jsonStr), status=200)
                    else:
                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "please select the valid date and time"
                        response.Result = False
                        response.Status = 400
                        response.HasError = True
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=400)

        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)