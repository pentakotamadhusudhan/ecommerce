import json
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import BloodBankChangePasswordSerializer, generateOTP
from partners.models import BloodBankModel, BloodBankOtpTable
from errormessage import Errormessage
import datetime
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class BloodBankChangePasswordView(generics.GenericAPIView):
    serializer_class = BloodBankChangePasswordSerializer

    def put(self, request, id):
        try:
            r = BloodBankModel.objects.get(id=id)
            password = make_password(request.data.get("RegisterPassword"))
            data = {'RegisterPassword': password}
            s = BloodBankChangePasswordSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            emailData = BloodBankModel.objects.get(id=id)
            email = emailData.BloodBankEmailId
            BloodBankName=emailData.BloodBankName
            otp = generateOTP()
            print(otp)
            created_at = datetime.datetime.now()
            print(created_at)
            user1 = BloodBankOtpTable(BloodBankId_id=id, otp=otp).save()
            htmly = get_template('user_forget_password_otp.html')
            d = {'otp': otp, 'created_at': created_at, "BloodBankName": BloodBankName}
            subject, from_email, to = 'Changed Blood Bank password successfully', settings.FROM_EMAIL, email
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
        except BloodBankModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
