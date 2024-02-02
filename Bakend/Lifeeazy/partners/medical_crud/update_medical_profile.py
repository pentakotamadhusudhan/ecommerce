import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from partners.serializer import MedicalProfileSerializer
from partners.models import Medicalprofile
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class MedicalUpdateProfileAPI(generics.GenericAPIView):
    serializer_class = MedicalProfileSerializer

    def put(self, request, id):
        try:
            r = Medicalprofile.objects.get(medicalid=id)
            State = request.data.get("State")
            City = request.data.get("City")
            Country = request.data.get('Country')
            Zipcode = request.data.get("Zipcode")
            Address = request.data.get("Address")
            PrimaryContactNumber = request.data.get("PrimaryContactNumber")

            data = {'State': State, 'City': City,'Country':Country, 'Zipcode': Zipcode, 'Address': Address,
                    'PrimaryContactNumber': PrimaryContactNumber }
            s = MedicalProfileSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
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
            response.Message = "Please enter the valid data to update"
            response.Result = ""
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
