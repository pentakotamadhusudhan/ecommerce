
import json
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import ChangePasswordSerializerAPI, generateOTP
from partners.models import InsuranceRegistrationModel, InsuranceOTP
from errormessage import Errormessage
import datetime
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class InsuranceChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializerAPI

    def put(self, request, id):
        try:
            r = InsuranceRegistrationModel.objects.get(id=id)
            RegisteredPassword = make_password(request.data.get("RegisteredPassword"))
            data = {'RegisteredPassword': RegisteredPassword}
            s = ChangePasswordSerializerAPI(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            emailData = InsuranceRegistrationModel.objects.get(id=id)
            email = emailData.InsuranceCompanyEmailId
            InsuranceCompanyName = emailData.InsuranceCompanyName
            RegisteredUsername = emailData.RegisteredUsername
            otp = generateOTP()
            print(otp)
            created_at = datetime.datetime.now()
            print(created_at)
            user1 = InsuranceOTP(InsuranceId_id=id, otp=otp).save()
            htmly = get_template('user_forget_password_otp.html')
            d = {'otp': otp, 'created_at': created_at, "InsuranceCompanyName": InsuranceCompanyName, "RegisteredUsername": RegisteredUsername}
            subject, from_email, to = 'Changed User password successfully', settings.FROM_EMAIL, email
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
        except InsuranceRegistrationModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)