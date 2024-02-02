from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField


# from django.db import MultipleChoiceField
# Create your models here.

class Clinic(models.Model):
    ClinicName_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                      message="firstname "
                                              "must string and should not be less than 3 and greater than 100")
    ClinicName = models.CharField(validators=[ClinicName_regex], max_length=30)
    ClinicRegistrationNumber = models.IntegerField()
    ClinicEmailId = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    ClinicContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    ClinicWebsiteUrl = models.URLField(max_length=200)
    RegisterUsername = models.CharField(validators=[ClinicName_regex], max_length=30)
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    RegisterPassword = models.CharField(validators=[password_regex], max_length=30)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=30)

    UploadClinicImages = models.ImageField()
    UploadRegisterationDocuments = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "Partner_clinic"


class ClinicProfile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    State = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Zipcode = models.IntegerField()
    Address = models.CharField(max_length=500)
    PrimaryContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    ClinicId = models.OneToOneField(Clinic, on_delete=models.CASCADE, related_name='Profile', primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "Clinic_Profile"


class AuthorizedModel(models.Model):
    ClinicId = models.ForeignKey(Clinic, related_name='Clinicid', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=255)
    EmailId = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    class Meta:
        db_table = "authorized_table"


LIST_PARTNERS = (
    ('Clinic', 'Clinic'),
    ('Hospital', 'Hospital'),
    ('Diagnostic', 'Diagnostic'),
    ('pharmacy', 'pharmacy'),
    ('Medical Surgical Equipment Provider', 'Medical Surgical Equipment Provider'),
    ('Blood Bank', 'Blood Bank'),
    ('Emergency Services', 'Emergency Services'),
    ('Gyms And Fitness Center', 'Gyms And Fitness Center'),
    ('Insurance', 'Insurance'),
)


class TypeOfPartner(models.Model):
    TypeOfPartners = models.CharField(max_length=100, choices=LIST_PARTNERS, default='Clinic')
    objects = models.manager

    class Meta:
        db_table = "Type_Of_Partner"


class BloodBankModel(models.Model):
    BloodBank_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="firstname "
                                             "must string and should not be less than 3 and greater than 100")
    BloodBankName = models.CharField(validators=[BloodBank_regex], max_length=255)
    BloodBankRegistrationNumber = models.IntegerField()
    BloodBankEmailId = models.EmailField(max_length=40)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    BloodBankContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    BloodBankWebsiteUrl = models.URLField(max_length=200)
    RegisterUsername = models.CharField(validators=[BloodBank_regex], max_length=30)
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    RegisterPassword = models.CharField(validators=[password_regex], max_length=100)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=100)

    UploadBloodBankImages = models.ImageField()
    UploadRegistrationDocuments = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "Partner_bloodbank"

    ####Gym Models####


class GymModel(models.Model):
    GymName_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                   message="gym name "
                                           "must string and should not be less than 3 and greater than 100")
    GymName = models.CharField(validators=[GymName_regex], max_length=30)
    GymRegistration = models.CharField(max_length=200)
    GymPhyarmacyEamilId = models.EmailField(max_length=50)
    contact_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                   message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                           "allowed.")
    GymContact = models.CharField(validators=[contact_regex], max_length=14, unique=True)
    GymWebsiteUrl = models.URLField(max_length=200)
    RegisterUsername = models.CharField(validators=[GymName_regex], max_length=30)
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    RegisterPassword = models.CharField(validators=[password_regex], max_length=30)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=30)

    UploadGymImages = models.ImageField()
    UploadRegisterationDocuments = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "Partner_Gym"


class GymOtpModel(models.Model):
    GymId = models.ForeignKey(GymModel, on_delete=models.CASCADE, related_name='gymotp', default=True)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager

    class Meta:
        db_table = "GymOtpTable"


class GymAuthorizedModel(models.Model):
    GymId = models.ForeignKey(GymModel, related_name='gymauthid', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=255)
    EmailId = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    class Meta:
        db_table = "gym_authorized_table"


####################pharmacy#################

class PharmacyModel(models.Model):
    Pharmacy_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                    message="PharmacyName "
                                            "must string and should not be less than 3 and greater than 100")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    PharmacyName = models.CharField(validators=[Pharmacy_regex], max_length=30)
    PharmacyRegistrationNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    PharmacyEmailId = models.EmailField(max_length=50)

    PharmacyContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    PharmacyWebsiteUrl = models.URLField(max_length=200)
    RegisterUsername = models.CharField(validators=[Pharmacy_regex], max_length=30)
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    RegisterPassword = models.CharField(validators=[password_regex], max_length=30)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=30)

    UploadPharmacyImages = models.ImageField()
    UploadRegisterationDocuments = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "Partner_Pharmacy"


class EmailVerifyTable(models.Model):
    UserId = models.ForeignKey(PharmacyModel, related_name='PharmacyModelId', on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager

    class Meta:
        db_table = "Pharmacyemailtb"


class BloodBankOtpTable(models.Model):
    BloodBankId = models.ForeignKey(BloodBankModel, related_name='bloodbank', on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    objects = models.Manager

    class Meta:
        db_table = "otp_bloodbank"


class MedicalEquipmentModel(models.Model):
    ProviderName_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                        message="firstname "
                                                "must string and should not be less than 3 and greater than 100")
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    ProviderName = models.CharField(validators=[ProviderName_regex], max_length=200)
    ProviderRegistration = models.CharField(max_length=100)
    ProviderEmailId = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    ProviderContact = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    ProviderWebsiteUrl = models.URLField(max_length=200)
    RegisteredUsername = models.CharField(validators=[ProviderName_regex], max_length=100)

    RegisteredPassword = models.CharField(validators=[password_regex], max_length=100)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=100)
    UploadEquipmentProviderImages = models.ImageField()
    UploadRegisteredDocuments = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = 'MedicalEquipment_table'


class MedicalOtpModel(models.Model):
    MedicalEquipmentId = models.ForeignKey(MedicalEquipmentModel, on_delete=models.CASCADE,
                                           related_name='MedicalEquipment', default=True)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager

    class Meta:
        db_table = "MedicalOtp_table"


class Medicalprofile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    State = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Zipcode = models.IntegerField()
    Address = models.CharField(max_length=500)
    PrimaryContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    medicalid = models.OneToOneField(MedicalEquipmentModel, on_delete=models.CASCADE, related_name='medicalprofile',
                                     primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "medical_profile"


class InsuranceRegistrationModel(models.Model):
    InsuranceCompanyName_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                                message="firstname "
                                                        "must string and should not be less than 3 and greater than 100")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")

    InsuranceCompanyName = models.CharField(validators=[InsuranceCompanyName_regex], max_length=30)
    InsuranceCompanyRegistrationNumber = models.IntegerField()
    InsuranceCompanyEmailId = models.EmailField(max_length=50)
    InsuranceCompanyContact = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    InsuranceCompanyWebsiteUrl = models.URLField(max_length=200)
    RegisteredUsername = models.CharField(validators=[InsuranceCompanyName_regex], max_length=30)
    RegisteredPassword = models.CharField(validators=[password_regex], max_length=100)
    ConfirmedPassword = models.CharField(validators=[password_regex], max_length=100)
    UploadInsuranceCompanyImages = models.ImageField()
    UploadRegistrationDocument = models.FileField()
    DeviceToken = models.CharField(max_length=255, default=None)
    objects = models.Manager

    class Meta:
        db_table = "Insurence_Company"


class AuthorisedPersonModel(models.Model):
    InsuranceId = models.ForeignKey(InsuranceRegistrationModel, related_name='InsurenceId', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    EmailId = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    PhoneNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    objects = models.Manager

    class Meta:
        db_table = "AuthorisedReg_table"


class AddProfileInsuranceModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    State = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Zipcode = models.IntegerField()
    Address = models.CharField(max_length=500)
    PrimaryContactNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    InsuranceId = models.OneToOneField(InsuranceRegistrationModel, on_delete=models.CASCADE, related_name='Insurance',
                                       primary_key=True)
    objects = models.Manager

    class Meta:
        db_table = "InsuranceProfile_table"


class InsuranceOTP(models.Model):
    InsuranceId = models.ForeignKey(InsuranceRegistrationModel, on_delete=models.CASCADE,
                                    related_name='InsuranceOtp', default=True)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    objects = models.Manager

    class Meta:       
        db_table = "InsuranceOtp_table"

class MedicalAuthorizedModel(models.Model):
    medicalid = models.OneToOneField(MedicalEquipmentModel, on_delete=models.CASCADE, related_name='medicalauthorized',
                                     primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=255)
    EmailId = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)


    class Meta:
        db_table = "medicalauthorized_table"

########BloodBank Authorized Person###############
class BloodBankAuthorizedModel(models.Model):
    BloodBankId = models.ForeignKey(BloodBankModel, related_name='Bloodbankdetails', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=255)
    EmailId = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)

    class Meta:
        db_table = "bloodbankauthorized_table"