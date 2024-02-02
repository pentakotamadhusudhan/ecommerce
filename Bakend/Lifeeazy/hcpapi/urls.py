from django.urls import path

from .views import *
from .views import HcpMobileIsRegistered

urlpatterns = [
    path('register/', HcpRegisterAPI.as_view(), name="Create a hcp user"),
    path('HcpProfile/', HcpProfileAPI.as_view(), name="Create a hcp profile"),
    path('HcpEducation/', HcpEducationalApi.as_view(), name="Create a hcp education"),
    path('HcpProfessional/', HcpProfessionalApi.as_view(), name="create a Hcp professional"),
    path('HcpClinic/', HcpClinicRegAPI.as_view(), name="Create a hcp clinic"),
    path('HcpClinicUpdate/<int:HcpId>/', HcpClinicUpdate.as_view()),
    path('Login/', HcpLoginAPI.as_view(), name="Login hcp user"),
    path('GetHcpData/', GetHcpList.as_view(), name="Get the all hcp data"),
    path('getHcpClinic/', GetHcpClinic.as_view(), name="Get the all doctor clinic"),
    path('GetHcpById/<int:id>/', GetHcpById.as_view(), name="get hcp data by the id"),
    path('ClinicById/<int:HcpId>/', GetClinicByID.as_view(), name="get clinic data by using doctor id"),
    path('HcpIsNumberRegistered/<str:MobileNumber>/', HcpMobileIsRegistered.as_view(), name='Number verification'),
    path('UpdateHcpProfile/<int:HcpId>/', HcpProfileUpdate.as_view(), name="Update hcp profile"),
    path('UpdateHcpEducation/<int:HcpId>/', HcpEducationUpdate.as_view(), name="Update hcp education"),
    path('UpdateHcpProfessional/<int:HcpId>/', HcpProfessionalUpdate.as_view(), name="Update hcp professional"),
    path('HcpChangePassword/<int:HcpId>/', HcpChangePasswordView.as_view(), name="Change the password"),
    path('GetAllDoctorsList', GetAllDoctorsList.as_view(), name="to get all the doctors with th schedule "),
    path('HcpPostBankDetails', HcpAddbankdetailsApi.as_view(), name="postbankdetails"),
    path('GetHcptBankDetails/<int:HcpId>', get_hcp_bank_details_by_id.as_view(), name="getbankdetails"),
    path('GetAllHcptBankDetails', get_all_hcp_bank_details.as_view(), name="getallbankdetails"),
    path('UpdateHcptBankDetails/<int:id>', update_hcp_bank_details.as_view(), name="updatebankdetails"),
    path('FCMApi/', FCMApi.as_view())
]
