from django.urls import path

from .views import Data, HcpPrescriptionRegAPI, HcpLabRecords, GetHcpLabRecordsAPI, HcpPresciptionById, \
    HcpLabRecordsById,HcpPresciptionByUserId

urlpatterns = [
    path('GetMedicalPrescriptionAPIList/', Data.as_view()),
    path('MedicalPrescriptionAPI/', HcpPrescriptionRegAPI.as_view()),
    path('LabPrescriptionApi/', HcpLabRecords.as_view()),
    path("GetLabPrescriptionAPIList/", GetHcpLabRecordsAPI.as_view()),
    path('GetPrescriptionById/<int:HcpId>/', HcpPresciptionById.as_view(), name="get the user prescription by id"),
    path('GetLabRecordsById/<int:HcpId>/', HcpLabRecordsById.as_view(), name="get the user lab records by id"),
    path("GetPresciptionByUserId/<int:UserId>/",HcpPresciptionByUserId.as_view())
]
