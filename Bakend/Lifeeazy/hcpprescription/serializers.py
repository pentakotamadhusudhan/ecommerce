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


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpProfessional')
        fields = ['Signature']


class UserLabRecordsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserlabRecords
        fields = ['HcpId', 'LabInvestigation', 'ImageInvestigation', 'Others', 'UserId']

    def create(self, validated_data):
        user = UserlabRecords.objects.create(HcpId=validated_data['HcpId'],
                                             LabInvestigation=validated_data['LabInvestigation'],
                                             ImageInvestigation=validated_data['ImageInvestigation'],
                                             Others=validated_data['Others'], UserId=validated_data['UserId'])
        user.save()
        return user


class PrescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPrescription
        fields = ['HcpId', 'DrugName', 'Quantity', 'Dosages', 'Frequency',
                  'Route', 'Instructions', 'NextFollowUp_Date', 'UserId']

    def create(self, validated_data):
        user = UserPrescription.objects.create(HcpId=validated_data['HcpId'],
                                               DrugName=validated_data['DrugName'],
                                               Quantity=validated_data['Quantity'],
                                               Dosages=validated_data['Dosages'],
                                               Frequency=validated_data['Frequency'],
                                               Route=validated_data['Route'],
                                               Instructions=validated_data['Instructions'],
                                               NextFollowUp_Date=validated_data['NextFollowUp_Date'],
                                               UserId=validated_data['UserId'])

        user.save()
        return user


class GetPrescriptionSerializers(serializers.ModelSerializer):
    HcpId = HcpSerializer(read_only=True)
    UserId = UserSerializer(read_only=True)

    class Meta:
        model = UserPrescription
        fields = ['HcpId', 'DrugName', 'Quantity', 'Dosages', 'Frequency',
                  'Route', 'Instructions', 'NextFollowUp_Date', 'UserId']


class GetLabrecordsSerializers(serializers.ModelSerializer):
    HcpId = HcpSerializer(read_only=True)
    UserId = UserSerializer(read_only=True)

    class Meta:
        model = UserlabRecords
        fields = ['HcpId', 'LabInvestigation', 'ImageInvestigation', 'Others', 'UserId']


class GetPrescriptionData(serializers.ModelSerializer):
    Hcpprescription = GetPrescriptionSerializers(many=True)
    Professional = ProfessionalSerializer(read_only=True)

    class Meta:
        model = apps.get_model('hcpapi', 'HcpModel')
        fields = ['Hcpprescription', 'Professional']


class GetLabSerializers(serializers.ModelSerializer):
    LabDetails = GetLabrecordsSerializers(many=True)
    Professional = ProfessionalSerializer(read_only=True)

    class Meta:
        model = apps.get_model('hcpapi', 'HcpModel')
        fields = ['LabDetails', 'Professional']


class GetPrescriptionSerializersbyuser(serializers.ModelSerializer):
    UserId = UserSerializer(read_only=True)
    HcpId = HcpSerializer(read_only=True)

    class Meta:
        model = UserPrescription
        fields = ['UserId', 'DrugName', 'Quantity', 'Dosages', 'Frequency',
                  'Route', 'Instructions', 'NextFollowUp_Date', 'HcpId']


class PersonalDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('user', 'UserProfile')
        fields = ['Gender']


class AddressDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('user', 'UserAddress')
        fields = ['Address']


class UserDetails(serializers.ModelSerializer):
    Profile = PersonalDetails(read_only=True)
    Address = AddressDetails(read_only=True)

    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = ['Username', 'MobileNumber', 'Profile', 'Address']


class HCPClinicdetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'Clinic')
        # fields='__all__'
        fields = ['ClinicName', 'Address']


class HCPEducationDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpEducational')
        fields = ['Degree']


class ProfessionalDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpProfessional')
        fields = ['MciNumber', 'MciStateCouncil', 'Specialization', 'AppointmentType', 'Signature']


# should include symptoms and allergies as well in get call

class DoctorDetails(serializers.ModelSerializer):
    Clinicdetails = HCPClinicdetails(read_only=True, many=True)
    Education = HCPEducationDetails(read_only=True)
    Professional = ProfessionalDetails(read_only=True)

    class Meta:
        model = apps.get_model('hcpapi', 'HcpModel')
        fields = ['Username', 'Email', 'MobileNumber', 'Education', 'Clinicdetails', 'Professional']


class Labdetails(serializers.ModelSerializer):
    class Meta:
        model = UserlabRecords
        fields = ['LabInvestigation', 'ImageInvestigation', 'Others']


class AllPrescriptionDetails(serializers.ModelSerializer):
    HcpId = DoctorDetails(read_only=True)
    UserId = UserDetails(read_only=True)

    class Meta:
        model = UserPrescription
        fields = '__all__'

