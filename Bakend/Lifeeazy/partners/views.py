from django.shortcuts import render
from .clinic_crud.clinic_register_api import ClinicRegisterAPI
from .clinic_crud.clinic_update_api import ClinicUpdateView
from .clinic_crud.clinic_update_by_registerusername import ClinicUpdateByRegisterUsernameView
from .clinic_crud.clinic_get_by_id import ClinicGetById
from .clinic_crud.clinic_getall_api import GetAllClinics
from .clinic_crud.clinic_addprofile_api import ClinicProfileAPI
from .clinic_crud.clinic_updateprofile_api import ClinicUpdateProfileAPI
from .clinic_crud.clinic_getallprofile_api import GetAllClinicProfile
from .clinic_crud.clinicprofile_getbyid_api import ClinicProfileGetById
from .clinic_crud.clinic_authorized_registration import AuthorizedRegisterAPI
from .clinic_crud.get_all_clinic_authorized_detailes import GetAuthorizedList
from .clinic_crud.update_authorized_detailes import UpdateAuthorizedDetailes
from .clinic_crud.clinic_authorized_getbyid_api import AuthorizedGetById
from .clinic_crud.clinic_login import ClinicLoginview
from .clinic_crud.partner_type_api import TypeOfPartnerAPI
from .clinic_crud.get_type_of_partner_api import GetTypeOfPartnerAPI


ClinicRegisterAPI()
ClinicLoginview()
ClinicUpdateView()
ClinicUpdateByRegisterUsernameView()
ClinicGetById()
GetAllClinics()
ClinicProfileAPI()
ClinicUpdateProfileAPI()
GetAllClinicProfile()
ClinicProfileGetById()
AuthorizedRegisterAPI()
GetAuthorizedList()
UpdateAuthorizedDetailes()
AuthorizedGetById()
TypeOfPartnerAPI()
GetTypeOfPartnerAPI()
# Insurance Company
from .insurance_crud.insurance_registration_api import InsuranceRegistrationAPI
from .insurance_crud.insurence_login_api import InsuranceLoginAPI
from .insurance_crud.authorised_person_reg_api import AuthorisedRegistrationAPI
from .insurance_crud.add_profile_insurance_api import AddProfileInsuranceAPI
from .insurance_crud.get_all_insurance_reg_api import GetAllInsuranceRegistrationAPI
from .insurance_crud.get_by_id_insurance_reg_api import GetByIdInsuranceRegistrationAPI
from .insurance_crud.update_insurance_reg_api import UpdateInsuranceRegistrationAPI
from .insurance_crud.change_password_insurancy_api import InsuranceChangePasswordView

InsuranceRegistrationAPI()
InsuranceLoginAPI()
AuthorisedRegistrationAPI()
AddProfileInsuranceAPI()
GetAllInsuranceRegistrationAPI()
UpdateInsuranceRegistrationAPI()
InsuranceChangePasswordView()






#medical equipment

from .medical_crud.medical_equipment_provider_registration_api import MedicalEquipmentPost
from .medical_crud.medical_equipment_login import MedicalLoginApi
from .medical_crud.medical_equipment_changepassword import MedicalEquipmentChangePasswordView
from .medical_crud.get_all_medical_equipment_detailes import GetAllMedicalEquipmentDetailes
from .medical_crud.get_by_id_medical_equipment_detailes import GetByIdMedicalEquipmentDetailes
from .medical_crud.update_medical_equipment import UpdateMedicalEquipmentDetailes
from .medical_crud.medicalequipment_add_profile import MedicalProfileAPI
from .medical_crud.medical_get_all_profile import GetAllMedicalequipment
from .medical_crud.medical_get_by_profileid_api import GetByProfileIdMedicalequipment
from .medical_crud.update_medical_profile import MedicalUpdateProfileAPI
from .medical_crud.medical_authorized_registration import MedicalAuthorizedRegisterAPI
from .medical_crud.medical_authorized_getbyid_api import MedicalAuthorizedGetById
from .medical_crud.get_all_medical_authorized_detailes import GetAllMedicalAuthorizedList
from .medical_crud.update_medical_authorized_detailes import UpdateMedicalAuthorizedDetailes

MedicalEquipmentPost()
MedicalLoginApi()
MedicalEquipmentChangePasswordView()
GetAllMedicalEquipmentDetailes()
GetByIdMedicalEquipmentDetailes()
UpdateMedicalEquipmentDetailes()
MedicalProfileAPI()
GetAllMedicalequipment()
GetByProfileIdMedicalequipment()
MedicalUpdateProfileAPI()
MedicalAuthorizedRegisterAPI()
MedicalAuthorizedGetById()
GetAllMedicalAuthorizedList()
UpdateMedicalAuthorizedDetailes()



#Blood Bank
from .bloodbank_crud.bloodbank_register_api import BloodBankRegisterAPI
from .bloodbank_crud.bloodbank_login import BloodBankLoginview
from .bloodbank_crud.bloodbank_change_password import BloodBankChangePasswordView
from .bloodbank_crud.get_all_bloodbank_api import GetAllBloodBanks
from .bloodbank_crud.get_bloodbanks_by_id import GetBloodBanksById
from .bloodbank_crud.update_registered_details import BloodbankUpdateView
from .bloodbank_crud.bloodbank_authorized_api import BloodBankAuthorizedRegisterAPI
from .bloodbank_crud.get_all_bloodbank_authorized import GetAllBloodBanksAuthorizedAPI
from .bloodbank_crud.get_byid_bloodbank_authorized import GetByIdBloodBanksAuthorizedAPI
from .bloodbank_crud.update_authorized_blodbank_details import BloodbankAuthorizedUpdateView

BloodBankRegisterAPI()
BloodBankLoginview()
BloodBankChangePasswordView()
GetAllBloodBanks()
GetBloodBanksById()
BloodbankUpdateView()
BloodBankAuthorizedRegisterAPI()
GetAllBloodBanksAuthorizedAPI()
GetByIdBloodBanksAuthorizedAPI()
BloodbankAuthorizedUpdateView()


#Gym Views####

from .gym_crud.gym_registration_api import GymRegistrationApi
from .gym_crud.gym_login_api import GymLoginview
from .gym_crud.get_gym_registration_details_api import GetAllGymRegistredDetailsApi
from .gym_crud.get_gym_registerd_details_by_id import GymDetailsGetById
from .gym_crud.gym_change_password_api import GymChangePasswordView
from .gym_crud.gym_registerd_details_update import GymUpdateView

GymRegistrationApi()
GymLoginview()
GetAllGymRegistredDetailsApi()
GymDetailsGetById()
GymChangePasswordView()
GymUpdateView()

##########################pharmacy#######################
from .pharmacy_crud.pharmacy_register_api import PharmacyRegisterAPI
from .pharmacy_crud.pharmacy_changepassword_api import PharmacyChangePasswordView
from .pharmacy_crud.pharmacy_login_api import PharmacyLoginview
from .pharmacy_crud.pharmacy_getall_api import GetAllPharmacy
from .pharmacy_crud.pharmacy_getbyid_api import PharmacyGetById
from .pharmacy_crud.pharmacy_registration_details_update import PharmacyUpdateAPI
PharmacyRegisterAPI()
PharmacyChangePasswordView()
PharmacyLoginview()
GetAllPharmacy()
PharmacyGetById()
PharmacyUpdateAPI()




