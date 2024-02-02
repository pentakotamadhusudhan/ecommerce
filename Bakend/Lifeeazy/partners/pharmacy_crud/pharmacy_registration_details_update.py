import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import PharmacySerializer,PharmacyupdateSerializer
from partners.models import PharmacyModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class PharmacyUpdateAPI(generics.GenericAPIView):
    serializer_class = PharmacySerializer

    def put(self, request, id):
        try:
            r = PharmacyModel.objects.get(id=id)
            PharmacyName = request.data.get("PharmacyName")
            PharmacyRegistrationNumber = request.data.get("PharmacyRegistrationNumber")
            PharmacyEmailId = request.data.get('PharmacyEmailId')
            PharmacyContactNumber = request.data.get("PharmacyContactNumber")
            PharmacyWebsiteUrl = request.data.get("PharmacyWebsiteUrl")
            RegisterUsername = request.data.get("RegisterUsername")
            RegisterPassword = request.data.get("RegisterPassword")
            ConfirmedPassword = request.data.get('ConfirmedPassword')
            UploadPharmacyImages = request.data.get("UploadPharmacyImages")
            UploadRegisterationDocuments = request.data.get("UploadRegisterationDocuments")
            #PrimaryContactNumber = request.data.get("PrimaryContactNumber")

            data = {'PharmacyName': PharmacyName, 'PharmacyRegistrationNumber': PharmacyRegistrationNumber,'PharmacyEmailId':PharmacyEmailId, 'PharmacyContactNumber': PharmacyContactNumber, 'PharmacyWebsiteUrl': PharmacyWebsiteUrl,
                    'RegisterUsername': RegisterUsername,'RegisterPassword': RegisterPassword,'ConfirmedPassword': ConfirmedPassword,'UploadPharmacyImages': UploadPharmacyImages,'UploadRegisterationDocuments': UploadRegisterationDocuments }
            s = PharmacyupdateSerializer(r, data=data, partial=True)
            print('hai')
            s.is_valid(raise_exception=True)
            print('hello')
            s.save()

            # Username = request.data.get('Username')
            # Email = request.data.get('Email')
            # htmly = get_template('update_familymember_notification.html')
            # d = {'Username': Username}
            # subject, from_email, to = 'Confirmation mail for UpdateFamilyMember', settings.FROM_EMAIL, Email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = True
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = ""
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
