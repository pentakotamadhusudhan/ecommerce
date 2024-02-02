from django.apps import apps
from rest_framework import serializers

from .models import HcpModel, HcpProfile, HcpEducational, HcpProfessional, Clinic, Addbankdetails

from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMultiAlternatives

from .models import HcpOtpModel
import math
import random


# class HcpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HcpModel
#         fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken']



class HcpProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpProfile
        fields = ['HcpId', 'ProfilePicture', 'State', 'City', 'Address', 'Pincode', 'Timezone']

    def create(self, validated_data):
        user = HcpProfile.objects.create(ProfilePicture=validated_data['ProfilePicture'],
                                         State=validated_data['State'], City=validated_data['City'],
                                         Address=validated_data['Address'], Pincode=validated_data['Pincode'],
                                         Timezone=validated_data['Timezone'], HcpId=validated_data['HcpId'])
        user.save()
        return user


class HcpEducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpEducational
        fields = ['Degree', 'CollegeUniversity', 'YearOfEducation', 'EducationalLocation', 'HcpId']

    def create(self, validated_data):
        user = HcpEducational.objects.create(Degree=validated_data['Degree'],
                                             CollegeUniversity=validated_data['CollegeUniversity'],
                                             YearOfEducation=validated_data['YearOfEducation'],
                                             EducationalLocation=validated_data['EducationalLocation'],
                                             HcpId=validated_data['HcpId'])
        user.save()
        return user


GENRE_CHOICES = (('Teleconsultation', 'Teleconsultation'), ('Home', 'Home'), ('In-clinic', 'In-clinic'),
                 )


class HcpProfessionalSerializer(serializers.ModelSerializer):
    AppointmentType = serializers.MultipleChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = HcpProfessional
        fields = ['ProfessionalId', 'ProfessionalExperienceInYears', 'CurrentStatus', 'MciNumber',
                  'MciStateCouncil', 'Specialization', 'AreaFocusOn', 'PatientsHandledPerDay',
                  'PatientsHandledPerSlot', 'AppointmentType', 'Signature', 'HcpId']

    def create(self, validated_data):
        user = HcpProfessional.objects.create(ProfessionalId=validated_data['ProfessionalId'],
                                              ProfessionalExperienceInYears=validated_data[
                                                  'ProfessionalExperienceInYears'],
                                              CurrentStatus=validated_data['CurrentStatus'],
                                              MciNumber=validated_data['MciNumber'],
                                              MciStateCouncil=validated_data['MciStateCouncil'],
                                              Specialization=validated_data['Specialization'],
                                              AreaFocusOn=validated_data['AreaFocusOn'],
                                              PatientsHandledPerDay=validated_data['PatientsHandledPerDay'],
                                              PatientsHandledPerSlot=validated_data['PatientsHandledPerSlot'],
                                              AppointmentType=validated_data['AppointmentType'],
                                              Signature=validated_data['Signature'],
                                              HcpId=validated_data['HcpId'])
        user.save()
        return user


class HcpProfessionalUpdateSerializer(serializers.ModelSerializer):
    AppointmentType = serializers.MultipleChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = HcpProfessional
        fields = ['ProfessionalId', 'ProfessionalExperienceInYears', 'CurrentStatus', 'MciNumber',
                  'MciStateCouncil', 'Specialization', 'AreaFocusOn', 'PatientsHandledPerDay',
                  'PatientsHandledPerSlot', 'AppointmentType', 'Signature']


class HcpAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpappointment', 'HcpScheduler')
        fields = ['ClinicId', 'FromDate', 'ToDate', 'FromTIme', 'ToTime', 'HcpId', 'TeleconsultationFees',
                  'InclinicFees',
                  'HomeFees']


class HcpSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = HcpModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                       Email=validated_data['Email'], Username=validated_data['Username'],
                                       Password=make_password(validated_data['Password']),
                                       MobileNumber=validated_data['MobileNumber'],
                                       DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class Userappointserializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('userappointment', 'AppointmentModel')
        fields=['DoctorId','Date','Time']



class HcpRegSerializer(serializers.ModelSerializer):
    Profile = HcpProfileSerializer(read_only=True)
    Professional = HcpProfessionalSerializer(read_only=True)
    Schedule = HcpAppointSerializer(read_only=True, many=True)
    Education = HcpEducationalSerializer(read_only=True)
    DoctorSchedule = Userappointserializer(read_only=True,many=True)

    class Meta:
        model = HcpModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken',
                  'Profile', 'Professional','DoctorSchedule','Schedule', 'Education']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = HcpModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                       Email=validated_data['Email'], Username=validated_data['Username'],
                                       Password=make_password(validated_data['Password']),
                                       MobileNumber=validated_data['MobileNumber'],
                                       DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class HcpLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpModel
        fields = ['Username', 'Password', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = HcpModel.objects.get(username=validated_data['Username'])
        user.device_token = validated_data['DeviceToken']
        user.save()
        return user


class HcpProfileUpdateSerializer(serializers.ModelSerializer):
    State = serializers.CharField(write_only=True, required=True)
    City = serializers.CharField(write_only=True, required=True)
    Address = serializers.CharField(write_only=True, required=True)
    Pincode = serializers.IntegerField(write_only=True, required=True)
    Timezone = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = HcpProfile
        fields = ['ProfilePicture', 'State', 'City', 'Address', 'Pincode', 'Timezone']


class HcpEducationUpdateSerializer(serializers.ModelSerializer):
    Degree = serializers.CharField(write_only=True, required=True)
    CollegeUniversity = serializers.CharField(write_only=True, required=True)
    YearOfEducation = serializers.CharField(write_only=True, required=True)
    EducationalLocation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = HcpEducational
        fields = ['Degree', 'CollegeUniversity', 'YearOfEducation', 'EducationalLocation']


class HcpPasswordSerializer(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = HcpModel
        fields = ['id', 'Password']

    def create(self, validated_data):
        user = HcpModel.objects.get(id=validated_data['id'])
        user.save()
        return user


class HcpClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id','ClinicName', 'Address', 'FromDate', 'ToDate', 'FromTime', 'ToTime', 'Fee', 'HcpId']

    def create(self, validated_data):
        user = Clinic.objects.create(ClinicName=validated_data['ClinicName'],
                                     Address=validated_data['Address'],
                                     FromDate=validated_data['FromDate'],
                                     ToDate=validated_data['ToDate'],
                                     FromTime=validated_data['FromTime'], ToTime=validated_data['ToTime'],
                                     Fee=validated_data['Fee'],
                                     HcpId=validated_data['HcpId'])

        user.save()
        return user

class HcpClinicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clinic
        fields = [ 'ClinicName', 'Address', 'FromDate', 'ToDate', 'FromTime', 'ToTime', 'Fee']


class FCMSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
    DeviceToken = serializers.CharField(max_length=2511)

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        DeviceToken = validated_data['DeviceToken']


class AddbankdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addbankdetails
        fields = ['HcpId', 'BankAccountNumber', 'BankName', 'IFSCCode', 'BankBranch', 'AccountNumber', 'PanNumber',
                  'UploadPancard', 'UploadDocuments', 'Remarks']


class UpdatebankdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addbankdetails
        fields = ['BankAccountNumber', 'BankName', 'IFSCCode', 'BankBranch', 'AccountNumber', 'PanNumber',
                  'UploadPancard', 'UploadDocuments', 'Remarks']


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

class TemplateSerializer(serializers.ModelSerializer):
    #UserId=RegSerializer()

    #Subject = serializers.CharField(max_length=50)

    class Meta:
        model=HcpOtpModel
        fields=['HCpId','otp']

    def create(self, validated_data):
        user = EmailVerifyTable.objects.create(UserId=validated_data['UserId'],otp=generateOTP())

        user.save()
        #print(user.otp)
        return user