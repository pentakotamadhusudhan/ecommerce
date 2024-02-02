from rest_framework import generics
from rest_framework.response import Response
from hcpappointment.serializers import HcpSchedulerUpdate
from genericresponse import GenericResponse
import json
from hcpappointment.models import HcpScheduler
from errormessage import Errormessage
from datetime import datetime
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class HcpSchedulerUpdateAPI(generics.GenericAPIView):
    serializer_class = HcpSchedulerUpdate

    def put(self, request, HcpId):
        try:

            clinic = apps.get_model("hcpapi", "Clinic")
            HcpEmail = apps.get_model("hcpapi", "HcpModel")
            hcpId = request.data.get("HcpId")
            emailData = HcpEmail.objects.get(id=hcpId)

            email = emailData.Email
            Firstname=emailData.Firstname
            Lastname=emailData.Lastname
            clinic_data = clinic.objects.filter(HcpId_id=HcpId).first()
            if clinic.objects.filter(HcpId_id=HcpId).first():
                d1 = request.data.get('FromDate')
                d2 = request.data.get('ToDate')
                t1 = request.data.get('FromTIme')
                t2 = request.data.get('ToTime')
                date = datetime.strptime(d1, '%Y-%m-%d')
                date1 = datetime.strptime(d2, '%Y-%m-%d')
                time = datetime.strptime(t1, '%H:%M:%S')
                time1 = datetime.strptime(t2, '%H:%M:%S')
                From_time = datetime.time(time)
                To_time = datetime.time(time1)
                From_date = datetime.date(date)
                To_date = datetime.date(date1)
                if clinic_data.FromDate <= From_date and clinic_data.ToDate >= To_date:
                    if clinic_data.FromTime <= From_time and clinic_data.ToTime >= To_time:
                        r = HcpScheduler.objects.get(HcpId=HcpId)
                        TeleconsultationFees = request.data.get("TeleconsultationFees")
                        InclinicFees = request.data.get("InclinicFees")
                        HomeFees = request.data.get("HomeFees")
                        data = {'FromDate': d1, 'ToDate': d2, 'FromTIme': t1, 'ToTime': t2,
                                'TeleconsultationFees': TeleconsultationFees, 'InclinicFees': InclinicFees,
                                'HomeFees': HomeFees}
                        s = HcpSchedulerUpdate(r, data=data, partial=True)
                        s.is_valid(raise_exception=True)
                        s.save()

                        Username = request.data.get('Username')
                        htmly = get_template('scheduler_update.html')
                        d = {'Username': Username,"Firstname":Firstname,"Lastname":Lastname}
                        subject, from_email, to = 'Congratulations You have Successfully updated your schedule', settings.FROM_EMAIL, email
                        html_content = htmly.render(d)
                        msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()

                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "Successful"
                        response.Result = data
                        response.Status = 200
                        response.HasError = False
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=200)
                    else:
                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "Your schedule time not match with your clinic time"
                        response.Result = []
                        response.Status = 400
                        response.HasError = False
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=400)
                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Your schedule date not match with your clinic date"
                    response.Result = []
                    response.Status = 400
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)

            else:
                r = HcpScheduler.objects.get(HcpId=HcpId)
                FromDate = request.data.get("FromDate")
                ToDate = request.data.get("ToDate")
                FromTIme = request.data.get("FromTIme")
                ToTime = request.data.get("ToTime")
                TeleconsultationFees = request.data.get("TeleconsultationFees")
                InclinicFees = request.data.get("InclinicFees")
                HomeFees = request.data.get("HomeFees")
                data = {'FromDate': FromDate, 'ToDate': ToDate, 'FromTIme': FromTIme, 'ToTime': ToTime,
                        'TeleconsultationFees': TeleconsultationFees, 'InclinicFees': InclinicFees, 'HomeFees': HomeFees}
                s = HcpSchedulerUpdate(r, data=data, partial=True)
                s.is_valid(raise_exception=True)
                s.save()

                Username = request.data.get('Username')
                Email = request.data.get('Email')
                htmly = get_template('scheduler_update.html')
                d = {'Username': Username}
                subject, from_email, to = 'Congratulations You have Successfully updated your schedule', settings.FROM_EMAIL, email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

        except HcpScheduler.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
