from django.db import models
from datetime import datetime


# Create your models here.
class AppointmentModel(models.Model):
    class Status(models.TextChoices):
        CREATED = 'CREATED'
        CONFIRMED = 'CONFIRMED'
        ACCEPTED = 'ACCEPTED'
        CANCELLED = 'CANCELLED'
        COMPLETED = 'COMPLETED'

    UserId = models.ForeignKey('user.UserModel', related_name='appointment', on_delete=models.CASCADE)
    DoctorId = models.ForeignKey('hcpapi.HcpModel', related_name='DoctorSchedule', on_delete=models.CASCADE)
    ScheduleId = models.ForeignKey('hcpappointment.HcpScheduler', related_name='Scheduleid', on_delete=models.CASCADE,null=True)

    FamilyMemberId = models.ForeignKey('user.FamilyMember', related_name='FamilyAppointment', on_delete=models.CASCADE,
                                       default=None, null=True)
    FamilyMemberAge = models.ForeignKey('user.FamilyMember', related_name='Familymemberage',
                                        on_delete=models.CASCADE, default=None, null=True)
    FamilyMemberGender = models.ForeignKey('user.FamilyMember', related_name='Familymembergender',
                                           on_delete=models.CASCADE, default=None, null=True)
    Date = models.DateField()
    Time = models.TimeField()
    Specialization = models.CharField(max_length=200)
    Status = models.CharField(max_length=10, choices=Status.choices)
    CurrentDate = models.DateTimeField(auto_now_add=True)
    AppointmentType = models.CharField(max_length=250, default=None)
    Fees = models.IntegerField(default=None)
    PrescriptionId = models.ForeignKey('hcpprescription.UserPrescription', related_name='Prescription', on_delete=models.CASCADE,default=None,null=True)
    objects = models.Manager

    class Meta:
        db_table = "User_Appointment"


class BillingModel(models.Model):
    TransactionId = models.CharField(max_length=1000)
    Date = models.DateField()
    Amount = models.IntegerField()
    UserId = models.ForeignKey('user.UserModel', related_name='userid', on_delete=models.CASCADE)
    DoctorId = models.ForeignKey('hcpapi.HcpModel', related_name='doctorbilling', on_delete=models.CASCADE)
    AppointmentType = models.CharField(max_length=250)
    objects = models.manager

    class Meta:
        db_table = "BillingTable"

Status = (
    ('InCompleted','InCompleted'),
    ('Half','Half'),
    ('Completed','Completed')

)

class VideoConsultModel(models.Model):
    AppointmentId = models.ForeignKey('AppointmentModel', related_name='VideoConsultModel', on_delete=models.CASCADE)
    CreatedDate = models.DateField()
    Status = models.CharField(max_length=100,choices=Status,default='InCompleted')
    Duration = models.CharField(max_length=100)
    objects = models.manager

    class Meta:
        db_table = "VideoConsult_table"

