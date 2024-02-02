from django.apps import apps
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"

    def create(self, validated_data):
        user = Clinic.objects.create(ClinicName=validated_data['ClinicName'],
                                     ClinicRegistrationNumber=validated_data['ClinicRegistrationNumber'],
                                     ClinicEmailId=validated_data['ClinicEmailId'],
                                     ClinicContactNumber=validated_data['ClinicContactNumber'],
                                     ClinicWebsiteUrl=validated_data['ClinicWebsiteUrl'],
                                     RegisterUsername=validated_data['RegisterUsername'],
                                     RegisterPassword=make_password(validated_data['RegisterPassword']),
                                     ConfirmedPassword=make_password(validated_data['ConfirmedPassword']),
                                     UploadClinicImages=validated_data['UploadClinicImages'],
                                     UploadRegisterationDocuments=validated_data['UploadRegisterationDocuments'],
                                     DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['RegisterUsername', 'RegisterPassword', 'DeviceToken']
        # extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = Clinic.objects.get(RegisterUsername=validated_data['RegisterUsername'])
        user.DeviceToken = validated_data['DeviceToken']
        user.save()
        return user


class AutherizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedModel
        fields = ['ClinicId', 'FirstName', 'LastName', 'EmailId', 'MobileNumber']

    def create(self, validated_data):
        user = AuthorizedModel.objects.create(ClinicId=validated_data['ClinicId'],
                                              FirstName=validated_data['FirstName'],
                                              LastName=validated_data['LastName'],
                                              EmailId=validated_data['EmailId'],
                                              MobileNumber=validated_data['MobileNumber'],
                                              )

        user.save()
        return user


class ClinicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['ClinicName', 'ClinicRegistrationNumber', 'ClinicEmailId', 'ClinicContactNumber', 'ClinicWebsiteUrl',
                  'RegisterUsername', 'RegisterPassword', 'ConfirmedPassword',
                  'UploadClinicImages', 'UploadRegisterationDocuments',
                  'DeviceToken']

    def create(self, validated_data):
        user = Clinic.objects.get(id=validated_data['id'])
        user.save()
        return user


class ClinicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicProfile
        fields = ['ClinicId', 'Country', 'State', 'City', 'Address', 'Zipcode', 'PrimaryContactNumber']

    def create(self, validated_data):
        user = ClinicProfile.objects.create(ClinicId=validated_data['ClinicId'],
                                            Country=validated_data['Country'],
                                            State=validated_data['State'], City=validated_data['City'],
                                            Address=validated_data['Address'], Zipcode=validated_data['Zipcode'],
                                            PrimaryContactNumber=validated_data['PrimaryContactNumber'])
        user.save()
        return user


class TypeOfPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfPartner
        fields = ['TypeOfPartners']

    def create(self, validated_data):
        user = TypeOfPartner.objects.create(TypeOfPartners=validated_data['TypeOfPartners'])
        user.save()
        return user


class InsuranceCompanyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRegistrationModel
        fields = ['id','InsuranceCompanyName', 'InsuranceCompanyRegistrationNumber', 'InsuranceCompanyEmailId',
                  'InsuranceCompanyContact', 'InsuranceCompanyWebsiteUrl', 'RegisteredUsername',
                  'RegisteredPassword', 'ConfirmedPassword', 'UploadInsuranceCompanyImages',
                  'UploadRegistrationDocument', 'DeviceToken']

    def create(self, validated_data):
        user = InsuranceRegistrationModel.objects.create(InsuranceCompanyName=validated_data['InsuranceCompanyName'],
                                                         InsuranceCompanyRegistrationNumber=validated_data[
                                                             'InsuranceCompanyRegistrationNumber'],
                                                         InsuranceCompanyEmailId=validated_data[
                                                             'InsuranceCompanyEmailId'],
                                                         InsuranceCompanyContact=validated_data[
                                                             'InsuranceCompanyContact'],
                                                         InsuranceCompanyWebsiteUrl=validated_data[
                                                             'InsuranceCompanyWebsiteUrl'],
                                                         RegisteredUsername=validated_data['RegisteredUsername'],
                                                         RegisteredPassword=make_password(
                                                             validated_data['RegisteredPassword']),
                                                         ConfirmedPassword=make_password(
                                                             validated_data['ConfirmedPassword']),
                                                         UploadInsuranceCompanyImages=validated_data[
                                                             'UploadInsuranceCompanyImages'],
                                                         UploadRegistrationDocument=validated_data[
                                                             'UploadRegistrationDocument'],
                                                         DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


#         # fields = ['InsuranceCompanyName','InsuranceCompanyRegistrationNumber','InsuranceCompanyEmailId','InsuranceCompanyContact','InsuranceCompanyWebsiteUrl','RegisteredUsername',
#         #           'RegisteredPassword','ConfirmedPassword','UploadInsuranceCompanyImages','UploadRegistrationDocument','DeviceToken']
#         #extra_kwargs = {'RegisteredPassword': {'write_only': True},'ConfirmedPassword': {'write_only': True},}


class InsuranceLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRegistrationModel
        fields = ['RegisteredUsername', 'RegisteredPassword', 'DeviceToken']
        extra_kwargs = {'RegisteredPassword': {'write_only': True}}

    def create(self, validated_data):
        user = InsuranceRegistrationModel.objects.get(username=validated_data['RegisteredUsername'])
        user.device_token = validated_data['DeviceToken']
        user.save()
        return user


from .models import InsuranceOTP
import math
import random


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class ChangePasswordSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRegistrationModel
        fields = ['id', 'RegisteredPassword']

    # def create(self, validated_data):
    #     user = ChangePasswordInsurance.objects.get(id=validated_data['id'])
    #     user.save()
    #     return user


class AddProfileInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProfileInsuranceModel
        fields = ['InsuranceId', 'State', 'City', 'Country', 'Zipcode', 'Address', 'PrimaryContactNumber']

    def create(self, validated_data):
        user = AddProfileInsuranceModel.objects.create(InsuranceId=validated_data['InsuranceId'],
                                                       State=validated_data['State'],
                                                       City=validated_data['City'], Country=validated_data['Country'],
                                                       Zipcode=validated_data['Zipcode'],
                                                       Address=validated_data['Address'],
                                                       PrimaryContactNumber=validated_data['PrimaryContactNumber'])
        user.save()
        return user


class AuthorisedRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorisedPersonModel
        fields = ['InsuranceId', 'FirstName', 'LastName', 'EmailId', 'PhoneNumber']

    def create(self, validated_data):
        user = AuthorisedPersonModel.objects.create(InsuranceId=validated_data['InsuranceId'],
                                                    FirstName=validated_data['FirstName'],
                                                    LastName=validated_data['LastName'],
                                                    EmailId=validated_data['EmailId'],
                                                    PhoneNumber=validated_data['PhoneNumber'])
        user.save()
        return user


class MedicalEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalEquipmentModel
        fields = '__all__'

    def create(self, validated_data):
        user = MedicalEquipmentModel.objects.create(ProviderName=validated_data['ProviderName'],
                                                    ProviderRegistration=validated_data['ProviderRegistration'],
                                                    ProviderEmailId=validated_data['ProviderEmailId'],
                                                    ProviderContact=validated_data['ProviderContact'],
                                                    ProviderWebsiteUrl=validated_data['ProviderWebsiteUrl'],
                                                    RegisteredUsername=validated_data['RegisteredUsername'],
                                                    RegisteredPassword=make_password(
                                                        validated_data['RegisteredPassword']),
                                                    ConfirmedPassword=make_password(
                                                        validated_data['ConfirmedPassword']),
                                                    UploadEquipmentProviderImages=validated_data[
                                                        'UploadEquipmentProviderImages'],
                                                    UploadRegisteredDocuments=validated_data[
                                                        'UploadRegisteredDocuments'])
        user.save()
        return user


class MedicalLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalEquipmentModel
        fields = ['RegisteredUsername', 'RegisteredPassword']


from .models import MedicalOtpModel
import math
import random


class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankModel
        fields = "__all__"

    def create(self, validated_data):
        user = BloodBankModel.objects.create(BloodBankName=validated_data['BloodBankName'],
                                             BloodBankRegistrationNumber=validated_data['BloodBankRegistrationNumber'],
                                             BloodBankEmailId=validated_data['BloodBankEmailId'],
                                             BloodBankContactNumber=validated_data['BloodBankContactNumber'],
                                             BloodBankWebsiteUrl=validated_data['BloodBankWebsiteUrl'],
                                             RegisterUsername=validated_data['RegisterUsername'],
                                             RegisterPassword=make_password(validated_data['RegisterPassword']),
                                             ConfirmedPassword=make_password(validated_data['ConfirmedPassword']),
                                             UploadBloodBankImages=validated_data['UploadBloodBankImages'],
                                             UploadRegistrationDocuments=validated_data['UploadRegistrationDocuments'],
                                             DeviceToken=validated_data['DeviceToken'])
        user.save()
        return user


import math
import random


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankOtpTable
        fields = ['BloodBankId', 'otp']

    def create(self, validated_data):
        user = BloodBankOtpTable.objects.create(BloodBankId=validated_data['BloodBankId'], otp=generateOTP())
        user.save()
        return user


class LoginSerializerBloodBank(serializers.ModelSerializer):
    class Meta:
        model = BloodBankModel
        fields = ['RegisterUsername', 'RegisterPassword', 'DeviceToken']
        # extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = BloodBankModel.objects.get(RegisterUsername=validated_data['RegisterUsername'])
        user.DeviceToken = validated_data['DeviceToken']
        user.save()
        return user


class BloodBankChangePasswordSerializer(serializers.ModelSerializer):
    RegisterPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BloodBankModel
        fields = ['id', 'RegisterPassword']

    def create(self, validated_data):
        user = BloodBankModel.objects.get(id=validated_data['id'])
        user.save()
        return user


class BloodBankUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankModel
        fields = "__all__"

    def create(self, validated_data):
        user = BloodBankModel.objects.get(id=validated_data['id'])
        user.save()
        return user


class MedicalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalEquipmentModel
        fields = ['id', 'RegisteredPassword', ]


class MedicalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicalprofile
        fields = ['medicalid', 'Country', 'State', 'City', 'Address', 'Zipcode', 'PrimaryContactNumber']

    def create(self, validated_data):
        user = Medicalprofile.objects.create(medicalid=validated_data['medicalid'],
                                             Country=validated_data['Country'],
                                             State=validated_data['State'], City=validated_data['City'],
                                             Address=validated_data['Address'], Zipcode=validated_data['Zipcode'],
                                             PrimaryContactNumber=validated_data['PrimaryContactNumber'])
        user.save()
        return user


###Gym Serializers###

class GymRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymModel
        fields = "__all__"

    def create(self, validated_data):
        user = GymModel.objects.create(GymName=validated_data['GymName'],
                                       GymRegistration=validated_data['GymRegistration'],
                                       GymPhyarmacyEamilId=validated_data['GymPhyarmacyEamilId'],
                                       GymContact=validated_data['GymContact'],
                                       GymWebsiteUrl=validated_data['GymWebsiteUrl'],
                                       RegisterUsername=validated_data['RegisterUsername'],
                                       RegisterPassword=make_password(validated_data['RegisterPassword']),
                                       ConfirmedPassword=make_password(validated_data['ConfirmedPassword']),
                                       UploadGymImages=validated_data['UploadGymImages'],
                                       UploadRegisterationDocuments=validated_data['UploadRegisterationDocuments'],
                                       DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class GymLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = GymModel
        fields = ['RegisterUsername', 'RegisterPassword', 'DeviceToken']

    def create(self, validated_data):
        user = GymModel.objects.get(RegisterUsername=validated_data['RegisterUsername'])
        user.DeviceToken = validated_data['DeviceToken']
        user.save()
        return user


class GymPasswordSerializer(serializers.ModelSerializer):
    RegisterPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = GymModel
        fields = ['id', 'RegisterPassword']

    def create(self, validated_data):
        user = GymModel.objects.get(id=validated_data['id'], otp=generateOTP())
        user.save()
        return user


class GymUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymModel
        fields = ['GymName', 'GymRegistration', 'GymPhyarmacyEamilId', 'GymContact', 'GymWebsiteUrl',
                  'RegisterUsername', 'RegisterPassword', 'ConfirmedPassword',
                  'UploadGymImages', 'UploadRegisterationDocuments',
                  'DeviceToken']

    def create(self, validated_data):
        user = GymModel.objects.get(id=validated_data['id'])
        user.save()
        return user


############################pharmacy#########################

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyModel
        fields = "__all__"

    def create(self, validated_data):
        user = PharmacyModel.objects.create(PharmacyName=validated_data['PharmacyName'],
                                            PharmacyRegistrationNumber=validated_data['PharmacyRegistrationNumber'],
                                            PharmacyEmailId=validated_data['PharmacyEmailId'],
                                            PharmacyContactNumber=validated_data['PharmacyContactNumber'],
                                            PharmacyWebsiteUrl=validated_data['PharmacyWebsiteUrl'],
                                            RegisterUsername=validated_data['RegisterUsername'],
                                            RegisterPassword=make_password(validated_data['RegisterPassword']),
                                            ConfirmedPassword=make_password(validated_data['ConfirmedPassword']),
                                            UploadPharmacyImages=validated_data['UploadPharmacyImages'],
                                            UploadRegisterationDocuments=validated_data['UploadRegisterationDocuments'],
                                            DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user


class ChangePasswordSerializerAPIPharmacy(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = PharmacyModel
        fields = ['id', 'Password']

    def create(self, validated_data):
        user = PharmacyModel.objects.get(id=validated_data['id'])
        user.save()
        return user


from .models import EmailVerifyTable


class PharmacyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyModel
        fields = ['RegisterUsername', 'RegisterPassword', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = PharmacyModel.objects.get(PharmacyName=validated_data['PharmacyName'])
        user.DeviceToken = validated_data['DeviceToken']
        user.save()
        return user


class PharmacyupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyModel
        fields = "__all__"

    def create(self, validated_data):
        user = PharmacyModel.objects.get(id=validated_data['id'])
        user.save()
        return user

class MedicalAutherizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAuthorizedModel
        fields = ['medicalid','FirstName','LastName', 'EmailId', 'MobileNumber']

    def create(self, validated_data):
        user = MedicalAuthorizedModel.objects.create(medicalid=validated_data['medicalid'],
                                              FirstName=validated_data['FirstName'],
                                              LastName=validated_data['LastName'],
                                              EmailId=validated_data['EmailId'],
                                              MobileNumber=validated_data['MobileNumber'],
                                              )

        user.save()
        return user

##############Bloodbank Authorized person##################
class BloodBankAuthorizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankAuthorizedModel
        fields = ['id','BloodBankId', 'FirstName', 'LastName', 'EmailId', 'MobileNumber']

    def create(self, validated_data):
        user = BloodBankAuthorizedModel.objects.create(BloodBankId=validated_data['BloodBankId'],
                                              FirstName=validated_data['FirstName'],
                                              LastName=validated_data['LastName'],
                                              EmailId=validated_data['EmailId'],
                                              MobileNumber=validated_data['MobileNumber'],
                                              )

        user.save()
        return user

class BloodBankAuthorizedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankAuthorizedModel
        fields = ['BloodBankId', 'FirstName', 'LastName', 'EmailId', 'MobileNumber']

    def create(self, validated_data):
        user = BloodBankAuthorizedModel.objects.get(id=validated_data['id'])
        user.save()
        return user