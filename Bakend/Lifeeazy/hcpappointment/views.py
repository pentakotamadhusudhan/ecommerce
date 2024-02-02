from .hcpappointment_crud.hcp_scheduler_regapi import HcpSchedulerRegAPI
from .hcpappointment_crud.create_user_appointment import CreateUserAppointment
from .hcpappointment_crud.doctor_appointment_get import DoctorAppointmentGet
from .hcpappointment_crud.appointment_get_by_hcpid import AppointmentGetByHcpId
from .hcpappointment_crud.get_appointment_status import GetAppointmentStatus
from .hcpappointment_crud.get_bydoctor_name import GetByDoctorName
from .hcpappointment_crud.doctor_status_update import DoctorStatusUpdate
from .hcpappointment_crud.fcm_api import FCMApi
from .hcpappointment_crud.get_by_doctor import GetByDoctor
from .hcpappointment_crud.doctor_billing_view import DoctorBillingView
from .hcpappointment_crud.hcp_scheduler_update_api import HcpSchedulerUpdateAPI
from .hcpappointment_crud.hcp_self_notes_api import HcpSelfNoteApi
from .hcpappointment_crud.get_self_notes_byid import GetSelfNotes
from .hcpappointment_crud.self_notes_update import SelfNoteUpdate
HcpSchedulerRegAPI()  # This is a post for registering the doctor slots
CreateUserAppointment()  # This is a post for creating a user appointment for user by the doctor
DoctorAppointmentGet()  # This is a get for getting all the schedule details of all the doctors
AppointmentGetByHcpId()  # This is a get for getting all the schedule details of a specific doctor based on doctor id
GetAppointmentStatus()  # This is a get for getting all the schedule details of a specific doctor based on doctor status
GetByDoctorName()  # This is a get for getting all the schedule details of a specific doctor based on doctor name
DoctorStatusUpdate()  # This is put for updating the status of the user appointment by the doctor
FCMApi()  # This is for fcm test
GetByDoctor()  # This is a get for getting all the user appointments for the doctors
DoctorBillingView()  # This is a get for getting the billing
HcpSchedulerUpdateAPI()
HcpSelfNoteApi()  # This is a post for self notes for the hcp
GetSelfNotes()  # To Get self notes based on doctor id
SelfNoteUpdate()  # To update the self notes based on id
