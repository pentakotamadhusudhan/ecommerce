import json
from rest_framework import generics
from rest_framework.response import Response
from hcpapi.serializer import HcpRegSerializer, HcpSerializer,generateOTP
from genericresponse import GenericResponse
from errormessage import Errormessage
from hcpapi.models import HcpOtpModel
from django.template.loader import get_template
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class HcpRegisterAPI(generics.GenericAPIView):
    serializer_class = HcpSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            Email = request.data.get('Email')
            Firstname=request.data.get("Firstname")
            Lastname=request.data.get("Lastname")
            otp = generateOTP()
            created_at = datetime.datetime.now()
            user1 = HcpOtpModel(HcpId_id=user.id, otp=otp).save()
            htmly = get_template('hcp_registration_otp.html')
            d = {'otp': otp, 'created_at': created_at , "Firstname":Firstname,"Lastname":Lastname}
            subject, from_email, to = 'Confirmation mail for Registration', settings.FROM_EMAIL, Email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result=HcpSerializer(user).data
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
