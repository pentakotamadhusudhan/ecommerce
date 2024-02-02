from rest_framework import generics
from rest_framework.response import Response
from partners.serializer import MedicalAutherizedSerializer
from genericresponse import GenericResponse
import json
from partners.models import MedicalAuthorizedModel
from errormessage import Errormessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.apps import apps


class UpdateMedicalAuthorizedDetailes(generics.GenericAPIView):
    serializer_class = MedicalAutherizedSerializer

    def put(self, request, id):

        try:
            r = MedicalAuthorizedModel.objects.get(medicalid=id)
            medicalid=request.data.get("medicalid")
            FirstName = request.data.get("FirstName")
            LastName = request.data.get("LastName")
            EmailId = request.data.get("EmailId")
            MobileNumber = request.data.get("MobileNumber")
            data = {'medicalid':medicalid,'FirstName': FirstName, 'LastName': LastName, 'EmailId': EmailId,
                    'MobileNumber': MobileNumber}
            s = MedicalAutherizedSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Username = request.data.get('Username')
            htmly = get_template('hcp_profile_update.html')
            d = {'Username': Username}
            subject, from_email, to = 'You have Successfully Updated the Profile', settings.FROM_EMAIL, EmailId
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
        except MedicalAuthorizedModel.DoesNotExist as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
