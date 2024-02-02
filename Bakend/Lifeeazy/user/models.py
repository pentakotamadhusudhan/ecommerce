from django.db import models
from django.core.validators import RegexValidator


class UserModel(models.Model):
    firstname_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="firstname "
                                             "must string and should not be less than 3 and greater than 12")
    lastname_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
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
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "User_Data"


TITLE = (
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Mr', 'Mr')
)

CHOICE_GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)

MARTIAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced')
)

BLOODGROUP = (
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('O-', 'O-')
)


class UserProfile(models.Model):
    UserId = models.OneToOneField(UserModel, related_name='Profile', on_delete=models.CASCADE)
    Title = models.CharField(max_length=10, choices=TITLE, default='Miss')
    Gender = models.CharField(max_length=10, choices=CHOICE_GENDER, default='Female')
    ProfilePicture = models.TextField()
    DOB = models.DateField(blank=True, null=True)
    MartialStatus = models.CharField(max_length=10, choices=MARTIAL_STATUS, default='single')
    BloodGroup = models.CharField(max_length=10, choices=BLOODGROUP, default='O+')

    objects = models.manager

    class Meta:
        db_table = "User_Profile"


class UserAddress(models.Model):
    UserId = models.OneToOneField(UserModel, related_name='Address', on_delete=models.CASCADE)
    Address = models.TextField(max_length=100)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    ZipCode = models.IntegerField()
    PrimaryNumber = models.CharField(max_length=50)
    objects = models.Manager

    class Meta:
        db_table = "User_Address"


class UserEmergencyDetails(models.Model):
    UserId = models.OneToOneField(UserModel, related_name='Emergency', on_delete=models.CASCADE)
    PersonName = models.CharField(max_length=50)
    RelationshipPatient = models.CharField(max_length=50)
    PrimaryNumber = models.CharField(max_length=50)
    MobileNumber = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    objects = models.Manager

    class Meta:
        db_table = "User_EmergencyDetails"


#
# class UserDependentProfile(models.Model):
#     UserId = models.OneToOneField(UserModel, related_name='DependentProfile', on_delete=models.CASCADE)
#     Title = models.CharField(max_length=10, choices=TITLE, default='Miss')
#     Gender = models.CharField(max_length=10, choices=CHOICE_GENDER, default='Female')
#     DOB = models.DateField(blank=True, null=True)
#     MartialStatus = models.CharField(max_length=10, choices=MARTIAL_STATUS, default='single')
#     BloodGroup = models.CharField(max_length=10, choices=BLOODGROUP, default='O+')
#     RelationshipToPatient = models.CharField(max_length=10)
#     objects = models.manager
#
#     class Meta:
#         db_table = "User_DependentProfile"
#
#
# class UserDependentAddress(models.Model):
#     UserId = models.OneToOneField(UserModel, related_name='DependentAddress', on_delete=models.CASCADE)
#     Address = models.TextField(max_length=100)
#     Country = models.CharField(max_length=50)
#     State = models.CharField(max_length=50)
#     City = models.CharField(max_length=50)
#     ZipCode = models.IntegerField()
#     PrimaryNumber = models.CharField(max_length=50)
#     objects = models.Manager
#
#     class Meta:
#         db_table = "User_DependentAddress"
#
#
# class UserDependentEmergencyDetails(models.Model):
#     UserId = models.OneToOneField(UserModel, related_name='DependentEmergency', on_delete=models.CASCADE)
#     PersonName = models.CharField(max_length=50)
#     RelationshipPatient = models.CharField(max_length=50)
#     PrimaryNumber = models.CharField(max_length=50)
#     MobileNumber = models.CharField(max_length=50)
#     Email = models.CharField(max_length=50)
#     objects = models.Manager
#
#     class Meta:
#         db_table = "User_DependentEmergencyDetails"

FamilyMember_Type = (
    ('ADULT', 'ADULT'),
    ('CHILD', 'CHILD'),
)
Alergies_type =(
    ('Drug','Drug'),
    ('Food','Food'),
    ('Others','Others')
)

Reactions =(
    ("Low","Low"),
    ("Moderate","Moderate"),
    ("Sever","Sever")

)


# added fieldss
class FamilyMember(models.Model):
    UserId = models.ForeignKey(UserModel, related_name='FamilyMemberProfile', on_delete=models.CASCADE)
    Title = models.CharField(max_length=10, choices=TITLE, default='Miss')
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=10, choices=CHOICE_GENDER, default='Female')
    ProfilePicture = models.TextField()
    Age = models.IntegerField(blank=True, null=True)
    FamilyMemberType = models.CharField(max_length=10, choices=FamilyMember_Type, default='ADULT')
    DOB = models.DateField(blank=True, null=True)
    MartialStatus = models.CharField(max_length=10, choices=MARTIAL_STATUS, default='single')
    BloodGroup = models.CharField(max_length=10, choices=BLOODGROUP, default='O+')
    RelationshipToPatient = models.CharField(max_length=10)
    IsEmergency = models.BooleanField()
    objects = models.manager

    class Meta:
        db_table = "FamilyMember"


class FamilyMemberAddress(models.Model):
    FamilyId = models.OneToOneField(FamilyMember, related_name='FamilyMemberAddress', on_delete=models.CASCADE)
    Address = models.TextField(max_length=100)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    ZipCode = models.IntegerField()
    PrimaryNumber = models.CharField(max_length=50)
    objects = models.Manager

    class Meta:
        db_table = "FamilyMemberAddress"


class Individualphysician(models.Model):
    UserId = models.ForeignKey(UserModel, related_name='UserProfile', on_delete=models.CASCADE)
    FamilyMemberId = models.ForeignKey('user.FamilyMember', related_name='Familymemberphysician', on_delete=models.CASCADE,
                                       default=None, null=True)
    PreferredPhysician = models.ForeignKey('hcpapi.HcpModel', related_name='individualphysician',
                                           on_delete=models.CASCADE)
    objects = models.Manager

    class Meta:
        db_table = "PreferredPhysicians"

class AnthropometricsModel(models.Model):
    UserId = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name="Anthropometrics")
    FamilyId = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, default=None,null=True,related_name="Anthropometricsfamilyid")
    Height = models.FloatField()
    Weight = models.FloatField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10, choices=CHOICE_GENDER, default='Female')
    Bmi = models.CharField(max_length=100)
    objects = models.Manager

    class Meta:
        db_table = "Bmicalucation"

class VitalsModel(models.Model):
    UserId = models.ForeignKey(UserModel, related_name='vital', on_delete=models.CASCADE)
    FamilyId = models.OneToOneField(FamilyMember, related_name='vitalFamilyid', on_delete=models.CASCADE,default=None,
                                    null=True)
    Height = models.IntegerField()
    weight = models.IntegerField()
    BMI = models.IntegerField()
    Temperature = models.CharField(max_length=255)
    spo2 = models.IntegerField()
    BP = models.FloatField()
    Pulse = models.IntegerField()

    class Meta:
        db_table = "vitalsdata"


class LabLevelsModel(models.Model):
    UserId = models.ForeignKey(UserModel, related_name='LabLevelUserid', on_delete=models.CASCADE)
    FamilyId = models.ForeignKey(FamilyMember, related_name='LabLevelFamilyid', on_delete=models.CASCADE, null=True,
                                 default=None)
    BloodGlucose = models.CharField(max_length=100)
    UrineGloucos = models.CharField(max_length=100)
    HbA1c = models.CharField(max_length=100)
    BloodCholesterol = models.CharField(max_length=100)
    HemoGlobin = models.CharField(max_length=100)
    UrineOutputIn24Hours = models.CharField(max_length=100)
    Others = models.CharField(max_length=100)

    class Meta:
        db_table = "LabLevelsTable"


class EmailVerifyTable(models.Model):
    UserId=models.ForeignKey(('user.UserModel'), related_name='UserId', on_delete=models.CASCADE)
    otp=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager
    class Meta:
        db_table="emailtb"

class Alergies(models.Model):
    AlergiesType = models.CharField(max_length=10, choices=Alergies_type, default='Drug')
    UserId = models.ForeignKey(UserModel, related_name='AlergiesUsername', on_delete=models.CASCADE)
    FamilyId = models.ForeignKey(FamilyMember, related_name='AllergiesFamilyid', on_delete=models.CASCADE, null=True,
                                 default=None)
    Reactions= models.CharField(max_length=10, choices=Reactions, default='Low')
    Comments=models.CharField(max_length=200)
    objects = models.Manager

    class Meta:
        db_table = "Alergies_Table"

# class MedicalSummeryModel(models.Model):
#     UserId = models.ForeignKey(UserModel, related_name='Userdetailes', on_delete=models.CASCADE)
#     Vitals = models.ForeignKey(VitalsModel, related_name='vital', on_delete=models.CASCADE)
#     LabLevels = models.ForeignKey(LabLevelsModel, related_name='LabLevelUserid', on_delete=models.CASCADE)
#     Anthropometrics = models.ForeignKey(AnthropometricsModel, related_name='Anthropometrics', on_delete=models.CASCADE)
#     Alergies = models.ForeignKey(Alergies, related_name='AlergiesUsername', on_delete=models.CASCADE)






