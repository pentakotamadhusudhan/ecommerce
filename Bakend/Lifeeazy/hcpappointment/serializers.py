from django.apps import apps
from rest_framework import serializers
from .models import *


class HcpSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpModel')
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'MobileNumber']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'MobileNumber']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('userappointment', 'AppointmentModel')
        fields = ['UserId', 'DoctorId', 'Date', 'Time', 'Specialization', 'Status', 'CurrentDate', 'AppointmentType',
                  'Fees']

    def to_representation(self, instance):
        rep = super(AppointmentSerializer, self).to_representation(instance)
        rep['DoctorId'] = instance.DoctorId.Username
        return rep


class HcpAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpScheduler
        fields = ['HcpId', 'FromDate', 'ToDate', 'FromTIme', 'ToTime', 'TeleconsultationFees', 'InclinicFees',
                  'HomeFees','AppointmentType']

    def create(self, validated_data):
        user = HcpScheduler.objects.create(HcpId=validated_data['HcpId'],

                                           FromDate=validated_data['FromDate'],
                                           ToDate=validated_data['ToDate'],
                                           FromTIme=validated_data['FromTIme'], ToTime=validated_data['ToTime'],
                                           TeleconsultationFees=validated_data['TeleconsultationFees'],
                                           InclinicFees=validated_data['InclinicFees'],
                                           HomeFees=validated_data["HomeFees"],AppointmentType=validated_data['AppointmentType'])
        user.save()
        return user


#
# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AppointmentModel
#         model = apps.get_model('userappointment', 'AppointmentModel')
#         fields = ['id']

class UserStatus(serializers.ModelSerializer):
    UserId = UserSerializer()

    class Meta:
        model = apps.get_model('userappointment', 'AppointmentModel')
        fields = ['id', 'CurrentDate', 'AppointmentType', 'Fees', 'UserId', 'DoctorId', 'Date', 'Time',
                  'Specialization',
                  'Status']


class DoctorStatus(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('userappointment', 'AppointmentModel')
        fields = ['Status']

    def create(self, validated_data):
        user_status = apps.get_model('userappointment', 'AppointmentModel')
        user = user_status.objects.get(id=validated_data['id'])
        user.save()
        return user


class FCMSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
    DeviceToken = serializers.CharField(max_length=2511)

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        DeviceToken = validated_data['DeviceToken']


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('userappointment', 'AppointmentModel')
        fields = ['Status']

    def create(self, validated_data):
        user_status = apps.get_model('userappointment', 'AppointmentModel')
        user = user_status.objects.get(id=validated_data['id'])
        user.save()
        return user


class DoctorBilling(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('userappointment', 'BillingModel')
        fields = ['TransactionId', 'Date', 'Amount', 'AppointmentType']


class HcpSchedulerUpdate(serializers.ModelSerializer):
    class Meta:
        model = HcpScheduler
        fields = ['HcpId', 'FromDate', 'ToDate', 'FromTIme', 'ToTime', 'TeleconsultationFees', 'InclinicFees',
                  'HomeFees']

    def create(self, validate_data):
        user = HcpScheduler.objects.get(HcpId=validate_data['HcpId'])
        user.save()
        return user


class HcpSelfNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpSelfNote
        fields = ['HcpId', 'AppointmentId', 'SelfNote']

    def create(self, validated_data):
        user = HcpSelfNote.objects.create(HcpId=validated_data["HcpId"], AppointmentId=validated_data["AppointmentId"],

                                          SelfNote=validated_data["SelfNote"])
        user.save()
        return user


class HcpUpdateSelfNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpSelfNote
        fields = ['HcpId', 'AppointmentId', "UpdatedDate", 'SelfNote']

    def create(self, validated_data):
        user = HcpSelfNote.objects.create(HcpId=validated_data['HcpId'], AppointmentId=validated_data["AppointmentId"],
                                          UpdatedDate=validated_data['UpdatedDate'],
                                          SelfNote=validated_data['SelfNote'])
        user.save()
        return user
