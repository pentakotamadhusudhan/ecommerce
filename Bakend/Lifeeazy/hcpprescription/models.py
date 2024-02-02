from django.db import models


# Create your models here.


class UserPrescription(models.Model):
    HcpId = models.ForeignKey('hcpapi.HcpModel', related_name='Hcpprescription', on_delete=models.CASCADE)
    DrugName = models.CharField(max_length=155)
    Quantity = models.IntegerField()
    Dosages=models.CharField(max_length=100,default=None)
    Route = models.CharField(max_length=155)
    Frequency = models.IntegerField()
    Instructions = models.TextField(default=None)
    NextFollowUp_Date=models.DateField()
    UserId = models.ForeignKey('user.UserModel', related_name='UserPrescription', on_delete=models.CASCADE)
    objects = models.Manager

    class Meta:
        db_table = "Prescriptions"


class UserlabRecords(models.Model):
    HcpId = models.ForeignKey('hcpapi.HcpModel', related_name='LabDetails', on_delete=models.CASCADE)

    LabInvestigation = models.CharField(max_length=255,default=None)
    ImageInvestigation = models.CharField(max_length=255,default=None)
    Others = models.CharField(max_length=255,default=None)
    UserId = models.ForeignKey('user.UserModel', related_name='UserlabDetails', on_delete=models.CASCADE)
    objects = models.Manager

    class Meta:
        db_table = "labRecords"



