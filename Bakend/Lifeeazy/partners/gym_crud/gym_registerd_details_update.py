import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import GymUpdateSerializer
from partners.models import GymModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class GymUpdateView(generics.GenericAPIView):
    serializer_class = GymUpdateSerializer

    def put(self, request, id):
        try:
            r = GymModel.objects.get(id=id)
            GymName = request.data.get("GymName")
            GymRegistration = request.data.get("GymRegistration")
            GymPhyarmacyEamilId = request.data.get('GymPhyarmacyEamilId')
            GymContact = request.data.get("GymContact")
            GymWebsiteUrl = request.data.get("GymWebsiteUrl")
            RegisterUsername = request.data.get("RegisterUsername")
            RegisterPassword = request.data.get("RegisterPassword")
            ConfirmedPassword = request.data.get("ConfirmedPassword")
            UploadGymImages = request.data.get("UploadGymImages")
            UploadRegisterationDocuments = request.data.get("UploadRegisterationDocuments")
            DeviceToken = request.data.get("DeviceToken")
            data = {'GymName': GymName, 'GymRegistration': GymRegistration,
                    'GymPhyarmacyEamilId': GymPhyarmacyEamilId, 'GymContact': GymContact,
                    'GymWebsiteUrl': GymWebsiteUrl,
                    'RegisterUsername': RegisterUsername, 'RegisterPassword': RegisterPassword,
                    'ConfirmedPassword': ConfirmedPassword,
                    "UploadGymImages": UploadGymImages,
                    "UploadRegisterationDocuments": UploadRegisterationDocuments, "DeviceToken": DeviceToken}
            s = GymUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            RegisterUsername = request.data.get('RegisterUsername')
            GymPhyarmacyEamilId = request.data.get('GymPhyarmacyEamilId')
            htmly = get_template('clinicreg.html')
            d = {'RegisterUsername': RegisterUsername}
            subject, from_email, to = 'Confirmation mail for Updateclinic', settings.FROM_EMAIL, GymPhyarmacyEamilId
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
