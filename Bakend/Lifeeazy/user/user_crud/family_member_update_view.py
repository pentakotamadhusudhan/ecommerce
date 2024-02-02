import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import FamilyMemberUpdateSerializer
from user.models import FamilyMember
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class FamilyMemberUpdateView(generics.GenericAPIView):
    serializer_class = FamilyMemberUpdateSerializer

    def put(self, request, id):
        try:
            r = FamilyMember.objects.get(id=id)
            Title = request.data.get("Title")
            Gender = request.data.get("Gender")
            Firstname = request.data.get('Firstname')
            Lastname = request.data.get("Lastname")
            Email = request.data.get("Email")
            DOB = request.data.get("DOB")
            ProfilePicture=request.data.get("ProfilePicture")
            MartialStatus = request.data.get("MartialStatus")
            BloodGroup = request.data.get("BloodGroup")
            RelationshipToPatient = request.data.get("RelationshipToPatient")
            IsEmergency = request.data.get('IsEmergency')
            data = {'Title': Title, 'Gender': Gender,'ProfilePicture':ProfilePicture, 'DOB': DOB, 'MartialStatus': MartialStatus,
                    'BloodGroup': BloodGroup, 'RelationshipToPatient': RelationshipToPatient,
                    "IsEmergency": IsEmergency, "Firstname": Firstname, "Lastname": Lastname, "Email": Email}
            s = FamilyMemberUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Username = request.data.get('Username')
            Email = request.data.get('Email')
            htmly = get_template('update_familymember_notification.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for UpdateFamilyMember', settings.FROM_EMAIL, Email
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
