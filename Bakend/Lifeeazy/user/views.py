from .user_crud.register_api import RegisterAPI
from .user_crud.profile_view import ProfileView
from .user_crud.address_view import AddressView
from .user_crud.emergency_view import EmergencyView
from .user_crud.family_member_view import FamilyMemberView
from .user_crud.family_member_address_view import FamilyMemberAddressView
from .user_crud.physician_view import PreferredPhysician
from .user_crud.login_view import Loginview
from .user_crud.profile_update import ProfileUpdate
from .user_crud.address_update import AddressUpdate
from .user_crud.emergency_update import EmergencyUpdate
from .user_crud.family_member_update_view import FamilyMemberUpdateView
from .user_crud.family_member_address_update_view import FamilyMemberAddressUpdateView
from .user_crud.change_password_view import ChangePasswordView
from .user_crud.get_user_list import GetUserList
from .user_crud.get_doctor_details import GetDoctorDetails
from .user_crud.get_preferred_physican import GetPreferredPhysican
from .user_crud.user_get_byId import UserGetById
from .user_crud.get_familymember_details import GetFamilyMembers
from .user_crud.user_mobile_isregistered import UserMobileIsRegisterd
from .user_crud.fcm_api import FCMApi
from .user_crud.get_family_by_userid import GetFamilyByUserId
from .user_crud.Anthropometrics_Get_FamilymemberId import AnthropometricsGetByFamilyById
from .user_crud.Anthropometrics_Post import AnthropometricsPost
from .user_crud.Anthropometrics_Update import AnthropometricsUpdate
from .user_crud.AnthropometricsGetUserId import AnthropometricsGetByUserId
from .user_crud.vitals_post import VitalsAPI
from .user_crud.get_vitals_byid import GetVitalsByUserId
from .user_crud.user_vitals_update import UserVitalsUpdateApi
from .user_crud.get_vitals_by_familyid import GetVitalsByFamilyId
from .user_crud.lab_levels_post import LabLevelPostAPI
from .user_crud.get_lab_levels import GetLabLevelsByUserId
from .user_crud.get_lab_levels_by_familyid import GetLabLevelsByFamilyId
from .user_crud.user_lab_levels_update import UserlablevelsUpdateApi
from .user_crud.allergies_post_api import AllergiesPost
from .user_crud.allergies_get_api import AllergiesGetApi
from .user_crud.allergies_getbyid_api import GetAllergiesByUserId
from .user_crud.get_allergies_by_familyid import GetAllergiesByFamilyId
from .user_crud.allergies_update_api import AllergiesUpdate
from .user_crud.get_all_medicalsummary import GetAllMedicalSummery
from .user_crud.get_by_familyid_medicalsummary import GetByFamilyidMedicalSummery
from .user_crud.get_by_id_medicalsummery import GetMedicalSummery


RegisterAPI()
ProfileView()
AddressView()
EmergencyView()
FamilyMemberView()
FamilyMemberAddressView()
PreferredPhysician()
Loginview()
GetUserList()
GetDoctorDetails()
GetPreferredPhysican()
UserGetById()
GetFamilyMembers()
UserMobileIsRegisterd()
ProfileUpdate()
AddressUpdate()
EmergencyUpdate()
FamilyMemberUpdateView()
FamilyMemberAddressUpdateView()
ChangePasswordView()
GetFamilyByUserId()
FCMApi()

AnthropometricsPost()
AnthropometricsGetByUserId()
AnthropometricsUpdate()
AnthropometricsGetByFamilyById()

VitalsAPI()
GetVitalsByUserId()
GetVitalsByFamilyId()
UserVitalsUpdateApi()
LabLevelPostAPI()
GetLabLevelsByUserId()
GetLabLevelsByFamilyId()
UserlablevelsUpdateApi()

AllergiesPost()
AllergiesGetApi()
GetAllergiesByUserId()
GetAllergiesByFamilyId()
AllergiesUpdate()
GetMedicalSummery()
GetAllMedicalSummery()
GetByFamilyidMedicalSummery()

