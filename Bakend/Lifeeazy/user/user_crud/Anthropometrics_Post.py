from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import AnthropometricsPostSerializer, AnthropometricsGetSerializer
from django.apps import apps
from user.models import AnthropometricsModel
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from errormessage import Errormessage


class AnthropometricsPost(generics.GenericAPIView):
    serializer_class = AnthropometricsPostSerializer

    def post(self, request, *args, **kwargs):
        try:
            userid = request.data.get('UserId')
            familyid = request.data.get('FamilyId')
            familyData = apps.get_model('user', 'FamilyMember')
            family = familyData.objects.filter(UserId_id=userid)
            FamilyMembers = []
            for i in family:
                FamilyMembers.append(int(i.id))
            print(FamilyMembers)
            if familyid is None:
                if AnthropometricsModel.objects.filter(UserId_id=userid).first():
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "UserId already exist try with another user"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()

                    userEmail = apps.get_model("user", "UserModel")
                    emailData = userEmail.objects.get(id=userid)
                    email = emailData.Email
                    htmly = get_template('anthropometrics_post_notification.html')
                    d = {'Username': emailData.Username}
                    subject, from_email, to = 'Confirmation mail for adding allergies for User', settings.FROM_EMAIL, email
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = AnthropometricsGetSerializer(user).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
            elif AnthropometricsModel.objects.filter(UserId_id=userid, FamilyId_id=familyid).first():
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "both userid and family id already exist"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
            elif int(familyid) in FamilyMembers:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()

                userEmail = apps.get_model("user", "UserModel")
                emailData = userEmail.objects.get(id=userid)
                email = emailData.Email
                htmly = get_template('anthropometrics_post_notification.html')
                d = {'Username': emailData.Username}
                subject, from_email, to = 'Confirmation mail for AnthropomentricsPost for Family member', settings.FROM_EMAIL, email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = AnthropometricsGetSerializer(user).data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "family member already exist"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = True
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
