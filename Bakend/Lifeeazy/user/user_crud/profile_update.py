import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import ProfileUpdateSerializer
from user.models import UserProfile, UserModel
from errormessage import Errormessage
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class ProfileUpdate(generics.GenericAPIView):
    serializer_class = ProfileUpdateSerializer

    def put(self, request, UserId):
        try:
            r = UserProfile.objects.get(UserId=UserId)
            userEmail = apps.get_model("user","UserModel")
            emailData = userEmail.objects.get(id=UserId)

            email = emailData.Email
            Title = request.data.get("Title")
            Gender = request.data.get("Gender")
            ProfilePicture = request.data.get("ProfilePicture")
            DOB = request.data.get("DOB")
            Martial_Status = request.data.get("MartialStatus")
            Blood_Group = request.data.get("BloodGroup")

            data = {'Title': Title, 'Gender': Gender, 'ProfilePicture': ProfilePicture, 'DOB': DOB,
                    'MartialStatus': Martial_Status,
                    'BloodGroup': Blood_Group}
            s = ProfileUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            Username = request.data.get('Username')

            htmly = get_template('updateprofilenotification.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for Profile Added successfully', settings.FROM_EMAIL, email
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
        except UserProfile.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
