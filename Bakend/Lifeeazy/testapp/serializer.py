from django.apps import apps
from rest_framework import serializers
from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"

    def create(self, validated_data):
        user = Topping.objects.create(name=validated_data['name'],vaccine=validated_data['vaccine'])
        user.save()
        return user

class SecondTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"

    def create(self, validated_data):
        user = Topping.objects.create(name=validated_data['name'],vaccine=validated_data['vaccine'])
        user.save()
        return user