from django.urls import path
                                        
from .views import *

urlpatterns = [
    path('ClinicUpdate/<int:id>/', ClinicUpdateView.as_view(), name="clinic update"),
    path('ClinicUpdateByRegisterUsername/<str:RegisterUsername>/', ClinicUpdateByRegisterUsernameView.as_view(), name="clinicupdatebyRegisterusername"),
    path("clinicGetById/<int:id>/", ClinicGetById.as_view()),
    path('GetAllClinics', GetAllClinics.as_view(), name="to get all clinics "),
    path('Register/', ClinicRegisterAPI.as_view(), name="Create a  clinic"),
    path('Login/',ClinicLoginview.as_view(),name="login"),
    path('AuthorizedApi/', AuthorizedRegisterAPI.as_view(), name="Create a  Authorized"),
    path('GetAuthorizedList/', GetAuthorizedList.as_view(), name="GetAuthorizedList"),
    path('UpdateAuthorizedDetailes/<int:id>', UpdateAuthorizedDetailes.as_view(), name="UpdateAuthorizedDetailes"),
    path('AuthorizedGetById/<int:Id>', AuthorizedGetById.as_view(), name="AuthorizedGetById"),
    path('ProfilePost/',ClinicProfileAPI.as_view(), name="Add Profile to Clinic"),
    path('ProfileUpdate/<int:ClinicId>',ClinicUpdateProfileAPI.as_view(),name = "Update Profile to Clinic "),
    path('GetAllClinicProfile/',GetAllClinicProfile.as_view(), name = " Get All Clinic Profile"),
    path('ClinicProfileGetById/<int:ClinicId>',ClinicProfileGetById.as_view(), name = " Get By Id Clinic Profile"),
    path('TypeOfPartnerAPI/',TypeOfPartnerAPI.as_view(), name = " TypeOfPartnerAPI"),
    path('GetAllTypeOfPartnerAPI/',GetTypeOfPartnerAPI.as_view(), name = " Get Type Of PartnerAPI"),


    #Medical equipment

    path('MedicalEquipmentPost/',MedicalEquipmentPost.as_view(), name = " Medical Equipment Post"),
    path('MedicalLoginApi/',MedicalLoginApi.as_view(), name = " Medical Equipment login"),
    path('MedicalEquipmentChangePasswordView/<int:id>/',MedicalEquipmentChangePasswordView.as_view(), name = " Medical Update Api"),
    path('GetAllMedicalEquipmentDetailes/',GetAllMedicalEquipmentDetailes.as_view(), name = " Get All Medical Equipment Detailes"),
    path('GetByIdMedicalEquipmentDetailes/<int:Id>',GetByIdMedicalEquipmentDetailes.as_view(), name = " Get All Medical Equipment Detailes"),
    path('UpdateMedicalEquipmentDetailes/<int:id>',UpdateMedicalEquipmentDetailes.as_view(), name = " Get All Medical Equipment Detailes"),
    path('MedicalProfileAPI/',MedicalProfileAPI.as_view(), name = "Medical Profile API"),
    path('GetAllMedicalequipmentprofile/',GetAllMedicalequipment.as_view(), name = "Get All Medical equipment"),
    path('GetByProfileIdMedicalequipment/<int:id>',GetByProfileIdMedicalequipment.as_view(), name = "Get All Medical equipment"),
    path('MedicalUpdateProfileAPI/<int:id>',MedicalUpdateProfileAPI.as_view(), name = "Medical Update Profile API"),
    path('MedicalAuthorizedRegisterAPI/',MedicalAuthorizedRegisterAPI.as_view(), name = "Medical Authorized Register API"),
    path('MedicalAuthorizedGetById/<int:Id>',MedicalAuthorizedGetById.as_view(), name = "Medical Authorized GetBy Id"),
    path('GetAllMedicalAuthorizedList/',GetAllMedicalAuthorizedList.as_view(), name = "Medical Authorized GetBy Id"),
    path('UpdateMedicalAuthorizedDetailes/<int:id>',UpdateMedicalAuthorizedDetailes.as_view(), name = "Update Medical Authorized Detailes"),

   #Blood Bank
    path('BloodBankRegister/',BloodBankRegisterAPI.as_view(),name="Registration"),
    path('BloodBankLogin/',BloodBankLoginview.as_view(),name="login bloodbank"),
    path('BloodBankChangePassword/<int:id>/',BloodBankChangePasswordView.as_view(),name="change password"),
    path('Getallbloodbanks/',GetAllBloodBanks.as_view(),name="get all blood banks"),
    path('GetbloodbanksById/<int:id>/',GetBloodBanksById.as_view(),name="get blood banks by id"),
    path('UpdateBloodBankDetails/<int:id>/',BloodbankUpdateView.as_view(),name="update blood bank details"),
    path('BloodBankAuthorizedRegisterAPI/',BloodBankAuthorizedRegisterAPI.as_view(),name="authorized blood bank"),
    path('GetAllBloodBanksAuthorized/',GetAllBloodBanksAuthorizedAPI.as_view(),name="get authorized bloodbank"),
    path('GetByIdBloodBanksAuthorized/<int:id>/',GetByIdBloodBanksAuthorizedAPI.as_view(),name="get by id authorized details"),
    path('BloodbankAuthorizedUpdateView/<int:id>/',BloodbankAuthorizedUpdateView.as_view(),name="update authorized bloodbank details"),
    # InsuranceCompany
    path('InsuranceRegistrationAPI/',InsuranceRegistrationAPI.as_view(), name = "Insurance Registration API"),
    path('InsuranceLoginAPI/',InsuranceLoginAPI.as_view(), name = "Insurance Login API"),
    path('InsuranceAuthorisedRegisterAPI/',AuthorisedRegistrationAPI.as_view(), name = "Authorised Register API"),
    path('AddProfileInsuranceAPI/',AddProfileInsuranceAPI.as_view(), name = "Add Profile InsuranceAPI"),
    path('GetAllInsuranceRegistrationAPI/',GetAllInsuranceRegistrationAPI.as_view(), name = "Get All Insurance Registration API"),
    path('GetByIdInsuranceRegistrationAPI/<int:id>',GetByIdInsuranceRegistrationAPI.as_view(), name = "Get By Id Insurance Registration API"),
    path('UpdateInsuranceRegistrationAPI/<int:id>',UpdateInsuranceRegistrationAPI.as_view(), name = "Update Insurance Registration API"),
    path('InsuranceChangePasswordView/<int:id>',InsuranceChangePasswordView.as_view(), name = "Insurance Change Password API"),
    # path('ClinicGetall/', ClinicGetAll.as_view(), name="Get All  clinics"),
    # path('ClinicGetByall/<int:Id>', ClinicGetById.as_view(), name="Get clinics by id"),

#####Gym Urls####
    path('GymRegistrationApi/', GymRegistrationApi.as_view(), name="Post Of Gym"),
    path('GymLoginview/', GymLoginview.as_view(), name="Login Of Gym"),
    path('GetAllGymRegistredDetailsApi/', GetAllGymRegistredDetailsApi.as_view(),
         name="Get All the registered details of the Gym"),
    path('GymDetailsGetById/<int:id>/', GymDetailsGetById.as_view(), name="Get Gym Details By Id"),
    path('GymChangePasswordView/<int:id>/', GymChangePasswordView.as_view(), name="Change Password of Gym"),
    path('GymUpdateView/<int:id>/', GymUpdateView.as_view(), name="Updating the Gym Registered Details"),
 ###############################Pharmacy############################
    path('PharmacyRegister/', PharmacyRegisterAPI.as_view(), name="Create a  Pharmacy"),
    path('PharmacyChnagepassword/<int:Id>/', PharmacyChangePasswordView.as_view(), name="PharmacyChangePasswordView"),
    path('Pharmacylogin', PharmacyLoginview.as_view(), name="PharmacyLoginview"),
    path('GetAllPharmacy', GetAllPharmacy.as_view(), name="GetAllClinicsPharmacy"),
    path("PharmacyGetById/<int:id>/", PharmacyGetById.as_view()),
    path("PharmacyUpdateAPI/<int:id>/", PharmacyUpdateAPI.as_view()),
]