import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import AllergiesUpdateSerializer
from user.models import Alergies
from errormessage import Errormessage
from django.apps import apps
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class AllergiesUpdate(generics.GenericAPIView):
    serializer_class = AllergiesUpdateSerializer

    def put(self, request, id):
        try:
            r = Alergies.objects.get(id=id)
            userEmail = apps.get_model("user","UserModel")
            UserId = request.data.get("UserId")
            emailData = userEmail.objects.get(id=UserId)

            email = emailData.Email
            UserId = request.data.get("UserId")
            FamilyId = request.data.get("FamilyId")
            AlergiesType = request.data.get("AlergiesType")
            Reactions = request.data.get("Reactions")
            Comments = request.data.get("Comments")


            data = {'UserId': UserId, 'FamilyId': FamilyId, 'AlergiesType': AlergiesType, 'Reactions': Reactions,
                    'Comments': Comments }
            s = AllergiesUpdateSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

            Username = request.data.get('Username')

            htmly = get_template('updateprofilenotification.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for  AllergiesUpdate successfully', settings.FROM_EMAIL, email
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
        except Alergies.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
