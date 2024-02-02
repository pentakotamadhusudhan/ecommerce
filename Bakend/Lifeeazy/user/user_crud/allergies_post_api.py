from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import AlergiesPostSerializer
from django.apps import apps
from user.models import Alergies
from errormessage import Errormessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from user.models import UserModel

class AllergiesPost(generics.GenericAPIView):
    serializer_class = AlergiesPostSerializer

    def post(self, request, *args, **kwargs):

        try:
            userid = request.data.get('UserId')
            familyid = request.data.get('FamilyId')
            familyData = apps.get_model('user', 'FamilyMember')
            family = familyData.objects.filter(UserId_id=userid)
            FamilyMembers = []
            for i in family:
                FamilyMembers.append(int(i.id))
            if familyid is None:
                if Alergies.objects.filter(UserId_id=userid).first():
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "UserId already exist please try another UserId"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()

                    userId = request.data.get("UserId")
                    emailData = UserModel.objects.get(id=userId)

                    email = emailData.Email
                    Username = request.data.get('Username')

                    htmly = get_template('lab_level_records_add.html')
                    d = {'Username': Username}
                    subject, from_email, to = 'Confirmation mail Allergies Added successfully for family member', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = AlergiesPostSerializer(user).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
            elif int(familyid) in FamilyMembers:
                if Alergies.objects.filter(UserId_id=userid, FamilyId_id=familyid).first():
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "both userid and family id already exist"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()

                    userId = request.data.get("UserId")
                    emailData = UserModel.objects.get(id=userId)

                    email = emailData.Email
                    Username = request.data.get('Username')

                    htmly = get_template('lab_level_records_add.html')
                    d = {'Username': Username}
                    subject, from_email, to = 'Confirmation mail for Allergies Added successfully for user', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()


                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = AlergiesPostSerializer(user).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "Allergies  not registerd because user and family member is not related"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)