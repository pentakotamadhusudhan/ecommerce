from django.apps import apps
from rest_framework import serializers, fields
from .models import AppointmentModel, BillingModel,VideoConsultModel

SchedulerData = apps.get_model('hcpappointment', 'HcpScheduler')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = ['UserId', 'DoctorId', 'ScheduleId', 'FamilyMemberAge', 'FamilyMemberGender',
                  'FamilyMemberId', 'Date', 'AppointmentType', 'Fees', 'Time', 'Specialization',
                  'Status', 'CurrentDate']

    def to_representation(self, instance):
        rep = super(AppointmentSerializer, self).to_representation(instance)
        rep['DoctorId'] = instance.DoctorId.Username
        return rep


class GetHcpDetails(serializers.ModelSerializer):
    class Meta:
        model = SchedulerData
        fields = '__all__'


class GetPrescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpprescription', 'UserPrescription')
        fields = '__all__'


class HcpDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpapi', 'hcpmodel')
        fields = '__all__'


class GetUserDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = '__all__'


class Appointments(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = ['UserId', 'DoctorId', 'ScheduleId', 'FamilyMemberAge', 'FamilyMemberGender',
                  'FamilyMemberId', 'Date', 'AppointmentType', 'Fees', 'Time', 'Specialization',
                  'Status', 'CurrentDate']

    # def to_representation(self, instance):
    #     rep = super(Appointments, self).to_representation(instance)
    #     rep['UserId'] = instance.UserId.Username
    #     return rep


class Appointment(serializers.ModelSerializer):
    DoctorId = HcpDetails()

    class Meta:
        model = AppointmentModel
        fields = ['UserId', 'DoctorId', 'ScheduleId', 'FamilyMemberAge', 'FamilyMemberGender',
                  'FamilyMemberId', 'Date', 'AppointmentType', 'Fees', 'Time', 'Specialization',
                  'Status', 'CurrentDate']


class GetAppointment(serializers.ModelSerializer):
    DoctorId = HcpDetails()
    PrescriptionId = GetPrescriptionSerializers()

    class Meta:
        model = AppointmentModel
        fields = ['UserId', 'DoctorId', 'ScheduleId', 'FamilyMemberAge', 'FamilyMemberGender',
                  'FamilyMemberId', 'Date', 'AppointmentType', 'Fees', 'Time', 'Specialization',
                  'Status', 'CurrentDate', 'PrescriptionId']


class FCMSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
    device_token = serializers.CharField(max_length=2511)


class BillingSerializer(serializers.ModelSerializer):
    # status=serializers.CharField(max_length=50)
    class Meta:
        model = BillingModel
        fields = ['TransactionId', 'Date', 'Amount', 'DoctorId', 'UserId', 'AppointmentType']

    def to_representation(self, instance):
        rep = super(BillingSerializer, self).to_representation(instance)
        rep['DoctorId'] = instance.DoctorId.Username
        return rep


class NewAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = ['UserId','DoctorId','ScheduleId','FamilyMemberId','FamilyMemberAge','FamilyMemberGender','Date',
                  'Time','Specialization','Status','AppointmentType','Fees','PrescriptionId']

    def create(self, validated_data):
        user = AppointmentModel.objects.create(UserId=validated_data['UserId'],
                                                DoctorId=validated_data['DoctorId'],ScheduleId=validated_data['ScheduleId'],
                                                FamilyMemberId=validated_data['FamilyMemberId'], FamilyMemberAge=validated_data['FamilyMemberAge'],
                                               FamilyMemberGender=validated_data['FamilyMemberGender'],Date=validated_data['Date'],
                                               Time=validated_data['Time'],Specialization=validated_data['Specialization'],
                                               Status=validated_data['Status'],
                                               AppointmentType=validated_data['AppointmentType'],
                                               Fees=validated_data['Fees'],PrescriptionId=validated_data['PrescriptionId'])
        user.save()
        return user
    def to_representation(self, instance):
        rep = super(NewAppointmentSerializer, self).to_representation(instance)
        rep['DoctorId'] = instance.DoctorId.Username
        return rep
class Prescriptionsserializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('hcpprescription', 'UserPrescription')
        fields = '__all__'
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         id =Prescriptionsserializer()
#         class Meta:
#             model=model = apps.get_model('hcpprescription', 'UserPrescription')
#             fields="__all__"
class VideoConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoConsultModel
        fields = ['AppointmentId','CreatedDate','Status','Duration']

    def create(self, validated_data):
        user = VideoConsultModel.objects.create(AppointmentId=validated_data['AppointmentId'],
                                            CreatedDate=validated_data['CreatedDate'],
                                            Status=validated_data['Status'], Duration=validated_data['Duration'])
        user.save()
        return user
