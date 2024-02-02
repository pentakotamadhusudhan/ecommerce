import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import AnthropometricsUpdateSerializer,AnthropometricsGetSerializer
from user.models import AnthropometricsModel
from django.apps import apps
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from anthropometricscalculation import bmiweight




class AnthropometricsUpdate(generics.GenericAPIView):
    serializer_class = AnthropometricsUpdateSerializer

    def put(self, request, id):
        try:
            r = AnthropometricsModel.objects.get(id=id)
            Height = float(request.data.get("Height"))
            Weight = float(request.data.get("Weight"))
            Age = request.data.get("Age")
            Gender = request.data.get("Gender")
            bmi = bmiweight((Height),(Weight))
            data = {'Height': Height, 'Weight': Weight, 'Age': Age,
                    'Gender': Gender,'Bmi': bmi}
            s = AnthropometricsGetSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
    

            userEmail = apps.get_model("user", "UserModel")
            emailData = userEmail.objects.get(id=r.UserId_id)
            email = emailData.Email
            Username = request.data.get('Username')
            htmly = get_template('anthropometrics_update_notification.html')
            d = {'Username': Username}
            subject, from_email, to = 'Confirmation mail for AnthropometricsUpdate', settings.FROM_EMAIL, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # return Response({
            #     "Message":"Successful",
            #     "Result":s.data
            # })
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = s.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except AnthropometricsModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Please enter the valid data to update"
            response.Result = ""
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)