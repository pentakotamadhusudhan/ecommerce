from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone


class HcpScheduler(models.Model):
    HcpId = models.ForeignKey('hcpapi.HcpModel', on_delete=models.CASCADE, related_name='Schedule')
    ClinicId = models.ForeignKey('hcpapi.Clinic', on_delete=models.CASCADE, related_name='ClinicData', default=None, null=True)
    FromDate = models.DateField()
    ToDate = models.DateField()
    FromTIme = models.TimeField()
    ToTime = models.TimeField()
    TeleconsultationFees = models.IntegerField(blank=True, default=None)
    InclinicFees = models.IntegerField(blank=True, default=None)
    HomeFees = models.IntegerField(blank=True, default=None)
    CurrentDate = models.DateTimeField(auto_now_add=True)
    AppointmentType = models.CharField(max_length=250)
    Fees = models.IntegerField()
    objects = models.Manager

    class Meta:
        db_table = "HCP_Scheduler"


class HcpSelfNote(models.Model):
    HcpId = models.ForeignKey('hcpapi.HcpModel', on_delete=models.CASCADE, related_name='selfnote')
    AppointmentId = models.ForeignKey('userappointment.AppointmentModel', on_delete=models.CASCADE,
                                         related_name="AppointmentId")
    CurrentDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now=True)
    SelfNote = models.TextField()
    objects = models.Manager

    class Meta:
        db_table = "Hcp_SelfNote"
