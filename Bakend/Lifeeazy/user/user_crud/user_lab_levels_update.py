from rest_framework import generics
from rest_framework.response import Response
from user.serializers import lablevelsUpdateSerializer
from genericresponse import GenericResponse
import json
from django.apps import apps
from user.models import LabLevelsModel
from errormessage import Errormessage
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives



class UserlablevelsUpdateApi(generics.GenericAPIView):
    serializer_class = lablevelsUpdateSerializer
    def put(self, request, Id):
        try:
            r = LabLevelsModel.objects.get(id=Id)
            UserId = request.data.get("UserId")
            FamilyId=request.data.get("FamilyId")
            BloodGlucose = request.data.get("BloodGlucose")
            UrineGloucos = request.data.get("UrineGloucos")
            HbA1c = request.data.get("HbA1c")
            BloodCholesterol = request.data.get("BloodCholesterol")
            HemoGlobin = request.data.get("HemoGlobin")
            UrineOutputIn24Hours = request.data.get("UrineOutputIn24Hours")
            Others = request.data.get("Others")

            data = {'UserId': UserId, 'FamilyId':FamilyId,'BloodGlucose': BloodGlucose, 'UrineGloucos': UrineGloucos,
                    'HbA1c': HbA1c,'BloodCholesterol': BloodCholesterol,'HemoGlobin': HemoGlobin, 'UrineOutputIn24Hours': UrineOutputIn24Hours,'Others': Others,}

            s = lablevelsUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            userEmail = apps.get_model("user", "UserModel")
            emailData = userEmail.objects.get(id=UserId)

            email = emailData.Email
            Username = request.data.get('Username')

            htmly = get_template('lab_level_records_update.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for lab level updated successfully', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except LabLevelsModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
