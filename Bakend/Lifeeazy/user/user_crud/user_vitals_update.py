from rest_framework import generics
from rest_framework.response import Response
from user.serializers import UserVitalsUpdateSerializer
from genericresponse import GenericResponse
import json
from django.apps import apps
from user.models import VitalsModel
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



class UserVitalsUpdateApi(generics.GenericAPIView):
    serializer_class = UserVitalsUpdateSerializer
    def put(self, request, Id):
        try:
            r = VitalsModel.objects.get(id=Id)
            UserId = request.data.get("UserId")
            FamilyId = request.data.get("FamilyId")
            Height = request.data.get("Height")
            weight = request.data.get("weight")
            BMI = request.data.get("BMI")
            Temperature = request.data.get("Temperature")
            spo2 = request.data.get("spo2")
            BP = request.data.get("BP")
            Pulse = request.data.get("Pulse")

            data = {'UserId': UserId, 'FamilyId':FamilyId,'Height': Height, 'weight': weight,
                    'BMI': BMI,'Temperature': Temperature,'spo2': spo2, 'BP': BP,'Pulse': Pulse,}

            data = {'UserId':UserId,'FamilyId':FamilyId,'Height': Height, 'weight': weight, 'BMI': BMI,
                    'Temperature': Temperature, 'spo2':spo2,'BP':BP,'Pulse':Pulse}

            s = UserVitalsUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            userEmail = apps.get_model("user", "UserModel")
            emailData = request.data.get("UserId")
            emailData = userEmail.objects.get(id=emailData)
            email = emailData.Email
            Firstname=emailData.Firstname
            Lastname=emailData.Lastname
            Username = request.data.get('Username')
            htmly = get_template('vitalsrecord_update_notification.html')
            d = {'Username': Username,"Firstname":Firstname,"Lastname":Lastname}
            subject, from_email, to = 'Confirmation mail for VitalsRecordUpdate for User', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = s.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except VitalsModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)


   
