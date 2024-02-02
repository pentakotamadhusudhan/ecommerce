from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import MedicalEquipmentSerializer
from genericresponse import GenericResponse
import json
from partners.models import MedicalEquipmentModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.apps import apps
from django.contrib.auth.hashers import make_password


class UpdateMedicalEquipmentDetailes(generics.GenericAPIView):
    serializer_class = MedicalEquipmentSerializer

    def put(self, request, id):

        try:
            r = MedicalEquipmentModel.objects.get(id=id)
            ProviderName=request.data.get("ProviderName")
            ProviderRegistration = request.data.get("ProviderRegistration")
            ProviderEmailId = request.data.get("ProviderEmailId")
            ProviderContact = request.data.get("ProviderContact")
            ProviderWebsiteUrl = request.data.get("ProviderWebsiteUrl")
            RegisteredUsername = request.data.get("RegisteredUsername")
            RegisteredPassword = make_password(request.data.get("RegisteredPassword"))
            ConfirmedPassword = make_password(request.data.get("ConfirmedPassword"))
            UploadEquipmentProviderImages = request.data.get("UploadEquipmentProviderImages")
            UploadRegisteredDocuments = request.data.get("UploadRegisteredDocuments")
            data = {'ProviderName':ProviderName,'ProviderRegistration': ProviderRegistration,
                    'ProviderEmailId': ProviderEmailId, 'ProviderContact': ProviderContact,
                    'ProviderWebsiteUrl': ProviderWebsiteUrl, 'RegisteredUsername': RegisteredUsername,
                    'RegisteredPassword': RegisteredPassword,
                    'ConfirmedPassword': ConfirmedPassword,'UploadEquipmentProviderImages': UploadEquipmentProviderImages,
                    'UploadRegisteredDocuments': UploadRegisteredDocuments,}
            s = MedicalEquipmentSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Username = request.data.get('Username')
            htmly = get_template('hcp_profile_update.html')
            d = {'Username': Username}
            subject, from_email, to = 'You have Successfully Updated the Profile', settings.FROM_EMAIL, ProviderEmailId
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except MedicalEquipmentModel.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
