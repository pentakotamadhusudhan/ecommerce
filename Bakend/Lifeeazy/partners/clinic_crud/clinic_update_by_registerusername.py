import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import ClinicUpdateSerializer
from partners.models import Clinic
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class ClinicUpdateByRegisterUsernameView(generics.GenericAPIView):
    serializer_class = ClinicUpdateSerializer

    def put(self, request, RegisterUsername):
        try:
            r = Clinic.objects.get(RegisterUsername=RegisterUsername)
            ClinicName = request.data.get("ClinicName")
            ClinicRegistrationNumber = request.data.get("ClinicRegistrationNumber")
            ClinicEmailId = request.data.get('ClinicEmailId')
            ClinicContactNumber = request.data.get("ClinicContactNumber")
            ClinicWebsiteUrl = request.data.get("ClinicWebsiteUrl")
            RegisterUsername = request.data.get("RegisterUsername")
            RegisterPassword=request.data.get("RegisterPassword")
            ConfirmedPassword=request.data.get("ConfirmedPassword")
            UploadClinicImages = request.data.get("UploadClinicImages")
            UploadRegisterationDocuments = request.data.get("UploadRegisterationDocuments")
            DeviceToken = request.data.get("DeviceToken")
            data = {'ClinicName': ClinicName, 'ClinicRegistrationNumber': ClinicRegistrationNumber,'ClinicEmailId':ClinicEmailId, 'ClinicContactNumber': ClinicContactNumber, 'ClinicWebsiteUrl': ClinicWebsiteUrl,
                    'RegisterUsername': RegisterUsername, 'RegisterPassword':RegisterPassword,'ConfirmedPassword': ConfirmedPassword,
                    "UploadClinicImages": UploadClinicImages, "UploadRegisterationDocuments": UploadRegisterationDocuments, "DeviceToken": DeviceToken}
            s = ClinicUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Username = request.data.get('Username')
            Email = request.data.get('Email')
            htmly = get_template('clinicreg.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for Updateclinic', settings.FROM_EMAIL, Email
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
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Please enter the valid data to update"
            response.Result = ""
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
