from .userappointment_crud.create_user_appointment import CreateUserAppointment
from .userappointment_crud.get_doctor_scheduler import GetDoctorScheduler
from .userappointment_crud.get_appointments import GetAppointments
from .userappointment_crud.get_appointment_byid import GetAppointmentById
from .userappointment_crud.by_status import ByStatus
from .userappointment_crud.fcm_api import FCMApi
from .userappointment_crud.billing_report import BillingReport
from .userappointment_crud.user_billing_view import UserBillingView
from .userappointment_crud.get_by_userid_prescription_details import GetAppointmentByUserIdPrescriptionDetails
from .userappointment_crud.get_by_userid_doctorid_prescription_details import \
    GetAppointmentByUserIdByHCPIdPrescriptionDetails
from .userappointment_crud.get_appointments_by_family_memberid import GetAppointmentByFamilyId
from .userappointment_crud.get_by_username import GetAppointmentByusername
from .userappointment_crud.video_consultency_api import VideoConsultAPI
from .userappointment_crud.update_video_consultancy_api import UpdateVideoConsultAPI
from .userappointment_crud.getall_video_consultancy_api import GetVideoConsult
from .userappointment_crud.getbyid_video_consultancy_api import GetByIdVideoConsult
from .userappointment_crud.getby_appointment_id_video_consultancy_api import GetByAppointmentIdVideoConsult

CreateUserAppointment()  # This is a post for an user to create a appointment
GetDoctorScheduler()  # This is a get for getting all the schedules of all the doctors
GetAppointments()  # This is a get for getting all the appointmets of all the doctors
GetAppointmentById()  # This is a get for getting all the appointmets of a specific doctor based on id
ByStatus()  # This is a get for getting the appointments by status
FCMApi()  # This is a test fcm
BillingReport()  # This is a post call for genarating the bill amount
UserBillingView()  # This is a get call for getting the user billing based on the user id
GetAppointmentByUserIdPrescriptionDetails()  # this is the get call for getting prescription details by userid
GetAppointmentByUserIdByHCPIdPrescriptionDetails()  # this is the get call for getting prescription details by userid and hcpid
GetAppointmentByFamilyId()  #this is a get call for getting the appointments of family members
GetAppointmentByusername()
VideoConsultAPI()
UpdateVideoConsultAPI()
GetVideoConsult()
GetByIdVideoConsult()
GetByAppointmentIdVideoConsult()
