from .hcpapi_crud.fcm_api import FCMApi
from .hcpapi_crud.get_all_doctors_list import GetAllDoctorsList
from .hcpapi_crud.get_clinic_by_id import GetClinicByID
from .hcpapi_crud.get_hcp_by_id import GetHcpById
from .hcpapi_crud.get_hcp_clinic import GetHcpClinic
from .hcpapi_crud.get_hcp_list import GetHcpList
from .hcpapi_crud.hcp_change_passwordview import HcpChangePasswordView
from .hcpapi_crud.hcp_clinic_regapi import HcpClinicRegAPI
from .hcpapi_crud.hcp_education_update import HcpEducationUpdate
from .hcpapi_crud.hcp_educational_api import HcpEducationalApi
from .hcpapi_crud.hcp_login_api import HcpLoginAPI
from .hcpapi_crud.hcp_mobile_isregistered import HcpMobileIsRegistered
from .hcpapi_crud.hcp_professional_api import HcpProfessionalApi
from .hcpapi_crud.hcp_professional_update import HcpProfessionalUpdate
from .hcpapi_crud.hcp_profile_api import HcpProfileAPI
from .hcpapi_crud.hcp_profile_update import HcpProfileUpdate
from .hcpapi_crud.hcp_register_api import HcpRegisterAPI
from .hcpapi_crud.hcp_bank_details import HcpAddbankdetailsApi
from .hcpapi_crud.get_hcp_bank_details_by_id import get_hcp_bank_details_by_id
from .hcpapi_crud.get_all_hcp_bank_details import get_all_hcp_bank_details
from .hcpapi_crud.update_hcp_bank_details import update_hcp_bank_details
from .hcpapi_crud.hcp_clinic_update import HcpClinicUpdate
FCMApi()
GetAllDoctorsList()  # To get all the doctor list with schedule timings which the doctor has assigned
GetClinicByID()  # To get all the clinic details of thedoctor based on doctor id
GetHcpById()  # To get all the personal details of the doctor based on doctor id
GetHcpClinic()  # To get all the clinics of the doctors
GetHcpList()  # To get all the doctors list
HcpChangePasswordView()  # To change the password of the doctor
HcpClinicRegAPI()  # To post the details of the clinic
HcpEducationUpdate()  # To update the educationl details
HcpEducationalApi()  # To post the educational details
HcpLoginAPI()  # This is for login of the user
HcpMobileIsRegistered()  # This is used for checking is the mobile is registerd or not
HcpProfessionalApi()  # To post the proffesinal details of the Doctor
HcpProfessionalUpdate()  # To Update the proffesinal details of the doctor
HcpProfileAPI()  # To post the profile details of the doctor
HcpProfileUpdate()  # To update the profile details of the doctor
HcpRegisterAPI()  # To post the registration of the doctor
HcpAddbankdetailsApi() # To post bank details of the doctor
get_hcp_bank_details_by_id() # To get bank details of doctor by id
get_all_hcp_bank_details() # To get all  bank details of doctor
update_hcp_bank_details() # To update doctor bank dertails
HcpClinicUpdate()






