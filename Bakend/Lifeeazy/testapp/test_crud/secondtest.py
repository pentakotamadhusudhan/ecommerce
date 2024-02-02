import json
from rest_framework import generics
from rest_framework.response import Response
from testapp.serializer import SecondTestSerializer
from genericresponse import GenericResponse
from errormessage import Errormessage
from django.template.loader import get_template
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from testapp.serializer import TestSerializer
from errormessage import Errormessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import get_template
from user.models import EmailVerifyTable
from django.shortcuts import render
from django.apps import apps
import datetime
from collections import Counter

counts = Counter
class SecondTestpost(generics.GenericAPIView):
    serializer_class = SecondTestSerializer
    def post(self, request, *args, **kwargs):
        try:
            Pizza = apps.get_model('testapp', 'Pizza')
            # family = Pizza.objects.filter(name_id=name)
            toppings = {}
            pizzas = Pizza.objects.filter(name="Hosipetal")
            for pizza in pizzas:
                for topping in pizza.toppings.all():
                    toppings[topping.name] = pizza.name
            sorted_toppings = toppings.keys()
            # sorted_toppings.sort()
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = SecondTestSerializer(user).data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)




