from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import GymPasswordSerializer, GymOtpModel,generateOTP
from genericresponse import GenericResponse
import json
from partners.models import GymModel
from errormessage import Errormessage
import datetime
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class GymChangePasswordView(generics.GenericAPIView):
    serializer_class = GymPasswordSerializer

    def put(self, request, id):
        try:
            r = GymModel.objects.get(id=id)
            RegisterPassword = make_password(request.data.get("RegisterPassword"))
            data = {'RegisterPassword': RegisterPassword}
            s = GymPasswordSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            # HcpEmail = apps.get_model("hcpapi", "HcpModel")
            # hcpId = request.data.get("HcpId")
            emailData = GymModel.objects.get(id=id)

            GymPhyarmacyEamilId = emailData.GymPhyarmacyEamilId
            GymName = emailData.GymName

            otp = generateOTP()
            print(otp)
            created_at = datetime.datetime.now()
            print(created_at)
            user1 = GymOtpModel(id=id, otp=otp).save()
            htmly = get_template('hcp_registration_otp.html')
            d = {'otp': otp, 'created_at': created_at, "GymName": GymName}
            subject, from_email, to = 'Changed password successfully', settings.FROM_EMAIL, GymPhyarmacyEamilId
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except GymModel.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
