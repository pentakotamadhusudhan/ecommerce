from django.urls import path
from .views import *

urlpatterns = [
    path('HcpSchedulerRegAPI/', HcpSchedulerRegAPI.as_view(), name="create doctor scheduler"),
    path('HcpCreateUserAppointment/', CreateUserAppointment.as_view(), name="create user appointment"),
    path('GetAllDoctorsSchedule/', DoctorAppointmentGet.as_view(), name="Get the all doctors"),
    path('GetDoctorsScheduleById/<int:HcpId>/', AppointmentGetByHcpId.as_view(), name="Get the doctor by the id"),
    path('HcpByStatus/<str:Status>/', GetAppointmentStatus.as_view(), name="get by the status"),
    path('HcpByDoctorName/<int:DoctorId>', GetByDoctorName.as_view(), name="Get the doctor name by the id"),
    path('DoctorStatusUpdate/<int:id>/', DoctorStatusUpdate.as_view(), name="Update the Doctor Status Update"),
    path('DoctorBillingView/<int:DoctorId>', DoctorBillingView.as_view()),
    path('FCMApi', FCMApi.as_view()),
    path('HcpSchedulerUpdateAPI/<int:HcpId>/',HcpSchedulerUpdateAPI.as_view()),
    path('HcpSelfNoteApi', HcpSelfNoteApi.as_view()),
    path('GetSelfNotes/<int:id>', GetSelfNotes.as_view()),
    path('SelfNoteUpdate/<int:id>', SelfNoteUpdate.as_view()),

]
