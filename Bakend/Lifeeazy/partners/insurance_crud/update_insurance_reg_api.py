from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import InsuranceCompanyRegistrationSerializer
from genericresponse import GenericResponse
import json
from partners.models import InsuranceRegistrationModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.apps import apps
from django.contrib.auth.hashers import make_password


class UpdateInsuranceRegistrationAPI(generics.GenericAPIView):
    serializer_class = InsuranceCompanyRegistrationSerializer

    def put(self, request, id):

        try:
            r = InsuranceRegistrationModel.objects.get(id=id)
            InsuranceCompanyName=request.data.get("InsuranceCompanyName")
            InsuranceCompanyRegistrationNumber = request.data.get("InsuranceCompanyRegistrationNumber")
            InsuranceCompanyEmailId = request.data.get("InsuranceCompanyEmailId")
            InsuranceCompanyContact = request.data.get("InsuranceCompanyContact")
            InsuranceCompanyWebsiteUrl = request.data.get("InsuranceCompanyWebsiteUrl")
            RegisteredUsernameRegisteredUsername = request.data.get("RegisteredUsernameRegisteredUsername")
            RegisteredPassword = make_password(request.data.get("RegisteredPassword"))
            ConfirmedPassword = make_password(request.data.get("ConfirmedPassword"))
            UploadInsuranceCompanyImages = request.data.get("UploadInsuranceCompanyImages")
            UploadRegistrationDocument = request.data.get("UploadRegistrationDocument")
            data = {'InsuranceCompanyName':InsuranceCompanyName,'InsuranceCompanyRegistrationNumber': InsuranceCompanyRegistrationNumber,
                    'InsuranceCompanyEmailId': InsuranceCompanyEmailId, 'InsuranceCompanyContact': InsuranceCompanyContact,
                    'InsuranceCompanyWebsiteUrl': InsuranceCompanyWebsiteUrl, 'RegisteredUsernameRegisteredUsername': RegisteredUsernameRegisteredUsername,
                    'RegisteredPassword': RegisteredPassword,
                    'ConfirmedPassword': ConfirmedPassword,'UploadInsuranceCompanyImages': UploadInsuranceCompanyImages,
                    'UploadRegistrationDocument': UploadRegistrationDocument,}
            s = InsuranceCompanyRegistrationSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            # Username = request.data.get('Username')
            # htmly = get_template('hcp_profile_update.html')
            # d = {'Username': Username}
            # subject, from_email, to = 'You have Successfully Updated the Profile', settings.FROM_EMAIL, ProviderEmailId
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except InsuranceRegistrationModel.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)