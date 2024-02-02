from django.urls import path
from .views import *

urlpatterns = [
    path("CreateUserAppointment/", CreateUserAppointment.as_view(), name="create an appointment by user"),
    path('GetAppointments/', GetAppointments.as_view(), name="get all the userappointment"),
    path('GetDoctorScheduler/', GetDoctorScheduler.as_view(), name="Get the doctor scheduler"),
    path('GetUserAppointmentGetById/<int:UserId>/', GetAppointmentById.as_view(),
         name="Get appointment by the user id"),
    path('UserAppointmentGetByStatus/<str:Status>/', ByStatus.as_view(), name='status'),
    path('BillingReport', BillingReport.as_view()),
    path('UserBillingView/<int:UserId>/', UserBillingView.as_view()),
    path('FCMApi', FCMApi.as_view()),
    path('GetPrescriptionDetailsByUserId/<int:UserId>/', GetAppointmentByUserIdPrescriptionDetails.as_view()),
    path('GetPrescriptionDetailsByUserIdHcpId/<int:UserId>/<int:HcpId>/',
         GetAppointmentByUserIdByHCPIdPrescriptionDetails.as_view()),
    path('GetAppointmentsbyusername/<str:Username>/', GetAppointmentByusername.as_view(), name="get all the GetAppointmentByusername"),
    path('GetAppointmentByFamilyId<int:FamilyMemberId>',GetAppointmentByFamilyId.as_view()),
    path('GetAppointments/<str:Username>/', GetAppointmentByusername.as_view(), name="get all the GetAppointmentByusername"),
    path('VideoConsultAPI/', VideoConsultAPI.as_view(), name="Video Consult API"),
    path('UpdateVideoConsultAPI/<int:id>', UpdateVideoConsultAPI.as_view(), name="Update Video Consult API"),
    path('GetVideoConsult/', GetVideoConsult.as_view(), name="Get Video Consult API"),
    path('GetByIdVideoConsult/<int:id>', GetByIdVideoConsult.as_view(), name="Get Video Consult API"),
    path('GetByAppointmentIdVideoConsult/<int:AppointmentId>', GetByAppointmentIdVideoConsult.as_view(), name="GetBy AppointmentId Video Consult"),

]
