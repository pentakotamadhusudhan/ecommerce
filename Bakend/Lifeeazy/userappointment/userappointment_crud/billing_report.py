from rest_framework import viewsets, generics
from rest_framework.views import APIView, Response
from userappointment.serializers import BillingSerializer
import json
from genericresponse import GenericResponse
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from user .models import UserModel



class BillingReport(generics.GenericAPIView):
    serializer_class = BillingSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            userId = request.data.get("UserId")
            emailData = UserModel.objects.get(id=userId)

            email = emailData.Email
            Username = request.data.get('Username')
            htmly = get_template('appointment_payment_success_notification.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for Appointment payment successful', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = BillingSerializer(user).data
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
