import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import BloodBankUpdateSerializer
from partners.models import BloodBankModel
from errormessage import Errormessage
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.hashers import make_password

class BloodbankUpdateView(generics.GenericAPIView):
    serializer_class = BloodBankUpdateSerializer

    def put(self, request, id):
        try:
            r = BloodBankModel.objects.get(id=id)
            email = request.data.get("BloodBankEmailId")
            BloodBankName = request.data.get("BloodBankName")
            BloodBankRegistrationNumber = request.data.get("BloodBankRegistrationNumber")
            BloodBankContactNumber = request.data.get("BloodBankContactNumber")
            BloodBankWebsiteUrl = request.data.get("BloodBankWebsiteUrl")
            RegisterUsername = request.data.get("RegisterUsername")
            RegisterPassword = make_password(request.data.get("RegisterPassword"))
            ConfirmedPassword=make_password(request.data.get("ConfirmedPassword"))
            UploadBloodBankImages=request.data.get("UploadBloodBankImages")
            UploadRegistrationDocuments=request.data.get("UploadRegistrationDocuments")
            DeviceToken=request.data.get("DeviceToken")

            data = {'BloodBankName': BloodBankName,
                    'BloodBankRegistrationNumber': BloodBankRegistrationNumber,
                    'BloodBankEmailId':email,
                    'BloodBankContactNumber': BloodBankContactNumber,
                    'BloodBankWebsiteUrl': BloodBankWebsiteUrl,
                    'RegisterUsername': RegisterUsername,
                    'RegisterPassword': RegisterPassword,
                    'ConfirmedPassword':ConfirmedPassword,
                    'UploadBloodBankImages':UploadBloodBankImages,
                    'UploadRegistrationDocuments':UploadRegistrationDocuments,
                    'DeviceToken':DeviceToken
                    }
            s = BloodBankUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            htmly = get_template('update_bloodbank_details.html')
            d = {'BloodBankName': BloodBankName}
            subject, from_email, to = 'Your BloodBank Details Updated Successfully', settings.FROM_EMAIL, email
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
        except BloodBankModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
