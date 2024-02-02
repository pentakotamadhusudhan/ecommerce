from django.db import models

from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField





class HcpModel(models.Model):
    firstname_regex = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="firstname "
                                             "must string and should not be less than 3 and greater than 12")
    lastname_regex = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                    message="lastname "
                                            "must string and should not be less than 3 and greater than 12")
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    Firstname = models.CharField(validators=[firstname_regex], max_length=30)
    Lastname = models.CharField(validators=[lastname_regex], max_length=30)
    Email = models.EmailField(max_length=50)
    Username = models.CharField(max_length=60, unique=True)
    Password = models.CharField(validators=[password_regex], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "HCP_Data"




class HcpOtpModel(models.Model):
    HcpId = models.ForeignKey(HcpModel, on_delete=models.CASCADE, related_name='hcpotp',default=True)
    otp=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager
    class Meta:
        db_table="HcpOtpTable"


class HcpProfile(models.Model):
    ProfilePicture = models.TextField()
    State = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Address = models.CharField(max_length=500)
    Pincode = models.CharField(max_length=255)
    Timezone = models.CharField(max_length=255)
    HcpId = models.OneToOneField(HcpModel, on_delete=models.CASCADE, related_name='Profile', primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "HCP_Profile"


class HcpEducational(models.Model):
    Degree = models.CharField(max_length=255)

    CollegeUniversity = models.CharField(max_length=255)
    YearOfEducation = models.IntegerField()
    EducationalLocation = models.CharField(max_length=255)
    HcpId = models.OneToOneField(HcpModel, on_delete=models.CASCADE, related_name='Education', primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "Hcp_Educational"


GENRE_CHOICES = (('Teleconsultation', 'Teleconsultation'), ('Home', 'Home'), ('In-clinic', 'In-clinic'),
                 )


class HcpProfessional(models.Model):
    ProfessionalId = models.CharField(max_length=255)
    ProfessionalExperienceInYears = models.IntegerField()
    CurrentStatus = models.BooleanField()
    MciNumber = models.IntegerField()
    MciStateCouncil = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=250)
    AreaFocusOn = models.CharField(max_length=50)
    PatientsHandledPerDay = models.IntegerField()
    PatientsHandledPerSlot = models.IntegerField()
    AppointmentType = MultiSelectField(max_length=200, choices=GENRE_CHOICES)
    Signature = models.TextField(default=None, null=True)
    HcpId = models.OneToOneField(HcpModel, on_delete=models.CASCADE, related_name='Professional', primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "Hcp_Professional"


class Clinic(models.Model):
    ClinicName = models.CharField(max_length=250)
    Address = models.CharField(max_length=200)
    FromDate = models.DateField()
    ToDate = models.DateField()
    FromTime = models.TimeField()
    ToTime = models.TimeField()
    Fee = models.IntegerField()
    HcpId = models.ForeignKey(HcpModel, on_delete=models.CASCADE, related_name='Clinicdetails')
    objects = models.Manager

    class Meta:
        db_table = "Hcp_Clinic"


class Addbankdetails(models.Model):
    HcpId = models.OneToOneField(HcpModel, on_delete=models.CASCADE, related_name='hcpbankdetails')
    BankAccountNumber = models.CharField(max_length=200)
    BankName = models.CharField(max_length=200)
    IFSCCode = models.CharField(max_length=200)
    BankBranch = models.CharField(max_length=50)
    AccountNumber = models.CharField(max_length=200)
    PanNumber = models.CharField(max_length=200)
    UploadPancard = models.TextField()
    UploadDocuments = models.TextField()
    Remarks = models.CharField(max_length=200)
    objects = models.Manager

    class Meta:
        db_table = "Hcp_Addbankdetails"
