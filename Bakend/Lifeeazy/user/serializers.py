from django.apps import apps
from rest_framework import serializers, fields
from .models import UserModel, UserProfile, UserAddress, UserEmergencyDetails, FamilyMember, Individualphysician, \
    VitalsModel, LabLevelsModel, EmailVerifyTable, FamilyMemberAddress, AnthropometricsModel, Alergies
from django.contrib.auth.hashers import make_password
from anthropometricscalculation import bmiweight

import math
import random


class FamilyMemberAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMemberAddress
        fields = ['FamilyId', 'Address', 'Country', 'State', 'City', 'ZipCode', 'PrimaryNumber']


class NewFamilyMemberAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMemberAddress
        fields = ['FamilyId', 'Address', 'Country', 'State', 'City', 'ZipCode', 'PrimaryNumber']


class GetFamilyMember(serializers.ModelSerializer):
    FamilyMemberAddress = FamilyMemberAddressSerializer(read_only=True)

    class Meta:
        model = FamilyMember
        fields = ['id', 'UserId', 'Title', 'Firstname', 'Lastname', 'Email', 'Gender', 'DOB', 'MartialStatus',
                  'BloodGroup',
                  'RelationshipToPatient', 'FamilyMemberAddress', 'IsEmergency']


class FamilyMemberSerializer(serializers.ModelSerializer):
    DOB = fields.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = FamilyMember
        fields = ['UserId', 'Title', 'Firstname', 'Lastname', 'Email', 'Gender', 'Age', 'DOB', 'MartialStatus',
                  'BloodGroup', 'ProfilePicture', 'FamilyMemberType',
                  'RelationshipToPatient', 'IsEmergency']

    def create(self, validated_data):
        user = FamilyMember.objects.create(UserId=validated_data['UserId'], Title=validated_data['Title'],
                                           Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                           Email=validated_data['Email'], Gender=validated_data['Gender'],
                                           DOB=validated_data['DOB'], Age=validated_data['Age'],
                                           MartialStatus=validated_data['MartialStatus'],
                                           FamilyMemberType=validated_data['FamilyMemberType'],
                                           BloodGroup=validated_data['BloodGroup'],
                                           ProfilePicture=validated_data['ProfilePicture'],
                                           RelationshipToPatient=validated_data['RelationshipToPatient'],
                                           IsEmergency=validated_data['IsEmergency'])
        age = validated_data['Age']
        if int(age) < 18:
            user.FamilyMemberType = "CHILD"
            user.MartialStatus = "Single"
            user.save()
            return user
        else:
            user.FamilyMemberType = "ADULT"
            user.save()
            return user


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['UserId', 'Address', 'Country', 'State', 'City', 'ZipCode', 'PrimaryNumber']


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmergencyDetails
        fields = ['UserId', 'PersonName', 'RelationshipPatient', 'PrimaryNumber', 'MobileNumber', 'Email']


class ProfileSerializer(serializers.ModelSerializer):
    DOB = fields.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = UserProfile
        fields = ['UserId', 'Title', 'Gender', 'ProfilePicture', 'DOB', 'MartialStatus', 'BloodGroup']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'MobileNumber']


class RegSerializer(serializers.ModelSerializer):
    Profile = ProfileSerializer(read_only=True)
    Address = AddressSerializer(read_only=True)
    Emergency = EmergencySerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken',
                  'Profile',
                  'Address',
                  'Emergency']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = UserModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                        Email=validated_data['Email'], Username=validated_data['Username'],
                                        Password=make_password(validated_data['Password']),
                                        MobileNumber=validated_data['MobileNumber'],
                                        DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['Username', 'Password', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.get(Username=validated_data['Username'])
        user.DeviceToken = validated_data['DeviceToken']
        user.save()
        return user


class ChangePasswordSerializerAPI(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'Password']

    def create(self, validated_data):
        user = UserModel.objects.get(id=validated_data['id'])
        user.save()
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'Title', 'Gender', 'ProfilePicture', 'DOB', 'MartialStatus', 'BloodGroup']

    def create(self, validated_data):
        user = UserProfile.objects.get(id=validated_data['id'])
        user.save()
        return user


class AddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['Address', 'Country', 'State', 'City', 'ZipCode', 'PrimaryNumber']

    def create(self, validated_data):
        user = UserAddress.objects.get(id=validated_data['id'])
        user.save()
        return user


class EmergencyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmergencyDetails
        fields = ['PersonName', 'RelationshipPatient', 'PrimaryNumber', 'MobileNumber', 'Email']

    def create(self, validated_data):
        user = UserEmergencyDetails.objects.get(id=validated_data['id'])
        user.save()
        return user


class FamilyMemberUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['UserId', 'Title', 'Firstname', 'Lastname', 'Email', 'Gender', 'ProfilePicture', 'DOB', 'Age',
                  'MartialStatus', 'BloodGroup',
                  'RelationshipToPatient', 'IsEmergency']

    def create(self, validated_data):
        user = FamilyMember.objects.get(id=validated_data['id'])
        user.save()
        return user


class FamilyMemberAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMemberAddress
        fields = ['Address', 'Country', 'State', 'City', 'ZipCode', 'PrimaryNumber']

    def create(self, validated_data):
        user = FamilyMemberAddress.objects.get(DependentId=validated_data['id'])
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


class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individualphysician
        fields = ['UserId', 'FamilyMemberId',
                  'PreferredPhysician']


class HcpProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpProfile')

        fields = ['State', 'City', 'Address', 'Pincode', 'Timezone']


class HcpEducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'HcpEducational')

        fields = ['Degree', 'CollegeUniversity', 'YearOfEducation', 'EducationalLocation', 'HcpId']


class HcpProfessionalSerializer(serializers.ModelSerializer):
    # AppointmentType = serializers.MultipleChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = apps.get_model('hcpapi', 'HcpProfessional')
        fields = ['ProfessionalId', 'ProfessionalExperienceInYears', 'CurrentStatus', 'MciNumber',
                  'MciStateCouncil', 'Specialization', 'AreaFocusOn', 'PatientsHandledPerDay',
                  'PatientsHandledPerSlot', 'AppointmentType', 'Signature', 'HcpId']


class HcpAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpappointment', 'HcpScheduler')
        fields = ['HcpId', 'FromDate', 'ToDate', 'FromTIme', 'ToTime', 'TeleconsultationFees', 'InclinicFees',
                  'HomeFees']


class HcpSerializer(serializers.ModelSerializer):
    Profile = HcpProfileSerializer()
    Education = HcpEducationalSerializer()
    Professional = HcpProfessionalSerializer()
    Schedule = HcpAppointSerializer()

    class Meta:
        model = apps.get_model('hcpapi', 'HcpModel')
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'MobileNumber', 'Profile', 'Education', 'Professional',
                  'Schedule']


class PhysicianSerializerGet(serializers.ModelSerializer):
    PreferredPhysician = HcpSerializer()

    # Profile = HcpProfileSerializer()
    # Address = HcpEducationalSerializer()
    # Professional = HcpProfessionalSerializer()
    class Meta:
        model = Individualphysician
        fields = ['UserId', 'FamilyMemberId'
                            'PreferredPhysician']


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalsModel
        fields = ['id', 'UserId', 'FamilyId', 'Height', 'weight', 'BMI', 'Temperature', 'spo2', 'BP',
                  'Pulse']


class GetVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalsModel
        fields = ['id', 'UserId', 'FamilyId', 'Height', 'weight', 'BMI', 'Temperature', 'spo2', 'BP',
                  'Pulse']


class UserVitalsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalsModel
        fields = ['UserId', 'FamilyId', 'Height', 'weight', 'BMI', 'Temperature', 'spo2', 'BP',
                  'Pulse']

    def create(self, validated_data):
        user = VitalsModel.objects.create(UserId=validated_data['UserId'], FamilyId=validated_data['FamilyId'],
                                          Height=validated_data['Height'],
                                          weight=validated_data['weight'], BMI=validated_data['BMI'],
                                          Temperature=validated_data['Temperature'],
                                          spo2=validated_data['spo2'], BP=validated_data['BP'],
                                          Pulse=validated_data['Pulse'])
        user.save()
        return user


class AnthropometricsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnthropometricsModel
        fields = ['Height', 'Weight', 'Age', 'Gender']


# class LabLevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabLevelsModel
#         fields = ['UserId', 'FamilyId', 'BloodGlucose', 'UrineGloucos', 'HbA1c', 'BloodCholesterol', 'HemoGlobin',
#                   'UrineOutputIn24Hours', 'Others']
#
#     def create(self, validated_data):
#         user = LabLevelsModel.objects.create(UserId=validated_data['UserId'], FamilyId=validated_data['FamilyId'],
#                                              BloodGlucose=validated_data['BloodGlucose'],
#                                              UrineGloucos=validated_data['UrineGloucos'],
#                                              HbA1c=validated_data['HbA1c'],
#                                              BloodCholesterol=validated_data['BloodCholesterol'],
#                                              HemoGlobin=validated_data['HemoGlobin'],
#                                              UrineOutputIn24Hours=validated_data['UrineOutputIn24Hours'],
#                                              Others=validated_data['Others'])
#         user.save()
#         return user


class LabLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabLevelsModel
        fields = "__all__"


class AnthropometricsGetSerializer(serializers.ModelSerializer):
    UserId = UserSerializer()

    class Meta:
        model = AnthropometricsModel
        fields = ['UserId', 'FamilyId', 'Height', 'Weight', 'Bmi', 'Age', 'Gender']


class AnthropometricsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnthropometricsModel
        fields = ['UserId', 'FamilyId', 'Height', 'Weight', 'Age', 'Gender']

    def create(self, validated_data):
        height = validated_data['Height']
        weight = validated_data['Weight']
        user = AnthropometricsModel.objects.create(Height=height, Weight=weight,
                                                   Age=validated_data['Age'], UserId=validated_data['UserId'],
                                                   Gender=validated_data['Gender'],
                                                   FamilyId=validated_data['FamilyId'])
        user.Bmi = bmiweight(height, weight)
        user.save()
        return user


class GetLabLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabLevelsModel
        fields = ['UserId', 'FamilyId', 'BloodGlucose', 'UrineGloucos', 'HbA1c', 'BloodCholesterol', 'HemoGlobin',
                  'UrineOutputIn24Hours', 'Others']


from .models import EmailVerifyTable
import math
import random


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class TemplateSerializer(serializers.ModelSerializer):
    # UserId=RegSerializer()

    # Subject = serializers.CharField(max_length=50)

    class Meta:
        model = EmailVerifyTable
        fields = ['UserId', 'otp']

    def create(self, validated_data):
        user = EmailVerifyTable.objects.create(UserId=validated_data['UserId'], otp=generateOTP())

        user.save()
        # print(user.otp)
        return user


#
# class lablevelsUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabLevelsModel
#         fields = ['id', 'UserId', 'FamilyId', 'BloodGlucose', 'UrineGloucos', 'HbA1c', 'BloodCholesterol', 'HemoGlobin', 'UrineOutputIn24Hours',
#                   'Others']
class lablevelsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabLevelsModel
        fields = ['UserId', 'FamilyId', 'BloodGlucose', 'UrineGloucos', 'HbA1c', 'BloodCholesterol', 'HemoGlobin',
                  'UrineOutputIn24Hours', 'Others']

        def create(self, validated_data):
            user = VitalsModel.objects.create(UserId=validated_data['UserId'], FamilyId=validated_data['FamilyId'],
                                              BloodGlucose=validated_data['BloodGlucose'],
                                              UrineGloucos=validated_data['UrineGloucos'],
                                              HbA1c=validated_data['HbA1c'],
                                              BloodCholesterol=validated_data['BloodCholesterol'],
                                              HemoGlobin=validated_data['HemoGlobin'],
                                              UrineOutputIn24Hours=validated_data['UrineOutputIn24Hours'],
                                              Pulse=validated_data['Others'])
            user.save()
            return user


class GetAlergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergies
        fields = ['UserId', "FamilyId", 'AlergiesType', 'Reactions', 'Comments']


class AlergiesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergies
        fields = ['UserId', "FamilyId", 'AlergiesType', 'Reactions', 'Comments']

    def create(self, validated_data):
        user = Alergies.objects.create(UserId=validated_data['UserId'], FamilyId=validated_data["FamilyId"],
                                       AlergiesType=validated_data['AlergiesType'],
                                       Reactions=validated_data['Reactions'],
                                       Comments=validated_data['Comments'])

        user.save()
        return user


class AllergiesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergies
        fields = ['UserId', "FamilyId", 'AlergiesType', 'Reactions', 'Comments']

        def create(self, validated_data):
            user = VitalsModel.objects.create(UserId=validated_data['UserId'], FamilyId=validated_data['FamilyId'],
                                              AlergiesType=validated_data['AlergiesType'],
                                              Reactions=validated_data['Reactions'],
                                              Comments=validated_data['Comments'])
            user.save()
            return user


class GetMedicalSumSerializer(serializers.ModelSerializer):
    vital = GetVitalSerializer(read_only=True, many=True)
    Anthropometrics = AnthropometricsGetSerializer(read_only=True, many=True)
    LabLevelUserid = LabLevelSerializer(read_only=True, many=True)
    AlergiesUsername = GetAlergiesSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ['vital',
                  'Anthropometrics', 'LabLevelUserid', 'AlergiesUsername']

class GetFamilyMedicalSumSerializers(serializers.ModelSerializer):
    vitalFamilyid = GetVitalSerializer(read_only=True)
    Anthropometricsfamilyid = AnthropometricsGetSerializer(read_only=True,many=True)
    LabLevelFamilyid = LabLevelSerializer(read_only=True, many=True)
    AllergiesFamilyid = GetAlergiesSerializer(read_only=True, many=True)

    class Meta:
        model = FamilyMember
        fields = ['vitalFamilyid',
                  'Anthropometricsfamilyid', 'LabLevelFamilyid', 'AllergiesFamilyid']

