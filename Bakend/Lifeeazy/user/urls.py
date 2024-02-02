from django.urls import path, include
# from .views import RegisterAPI, Loginview, GetUserList, UserMobileIsRegisterd, EmergencyView, ChangePasswordView, \
#     AddressView, \
#     ProfileView, UserGetById, ProfileUpdate, Dependent_AddressView, Dependent_ProfileView, \
#     Dependent_ProfileUpdate, DependentAddressUpdate, EmergencyUpdate, AddressUpdate, \
#     GetDoctorDetails, FCMApi, GetPreferredPhysican, PreferredPhysician, GetFamilyMembers
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Register/', RegisterAPI.as_view(), name='Register the user'),
    path('Profile/', ProfileView.as_view(), name='Create the user profile'),
    path('Address/', AddressView.as_view(), name='Create the user address'),
    path('EmergencyDetails/', EmergencyView.as_view(), name='Create the Emergency details'),
    path('AddFamilyMemberView/', FamilyMemberView.as_view(), name='Create the dependent profile'),
    path('AddFamilyMemberAddressView/', FamilyMemberAddressView.as_view(), name="Create the dependent address"),
    # path('DependentEmergency/', Dependent_EmergencyView.as_view(), name='Create the dependent emergency details'),
    path('PreferredPhysician/', PreferredPhysician.as_view(), name='physician'),
    path('Login/', Loginview.as_view(), name='Login the user'),
    path('GetUserData/', GetUserList.as_view(), name='Get the user data'),
    path('GetDoctorsData/', GetDoctorDetails.as_view(), name="get the doctor data"),
    path('GetUserById/<int:Id>/', UserGetById.as_view(), name='GEt the user data by id'),
    path('GetFamilyMember/', GetFamilyMembers.as_view(), name="get the family members"),
    path('GetPreferredPhysician/<int:UserId>', GetPreferredPhysican.as_view(), name='getphysician'),
    path('UserIsNumberRegistered/<str:MobileNumber>/', UserMobileIsRegisterd.as_view(),
         name='mobile number verification'),
    path('UserChangePassword/<int:Id>/', ChangePasswordView.as_view(), name='change password by the views'),
    path('UserProfileUpdate/<int:UserId>/', ProfileUpdate.as_view(), name='update user profile'),
    path('UserAddressUpdate/<int:UserId>/', AddressUpdate.as_view(), name='update user address'),
    path('UserEmergencyDetailsUpdate/<int:UserId>/', EmergencyUpdate.as_view(), name='update user emergency'),
    path('FamilyMemberUpdateView/<int:id>/', FamilyMemberUpdateView.as_view(),
         name='update user dependent profile'),
    path('FamilyMemberAddressUpdateView/<int:FamilyId>/', FamilyMemberAddressUpdateView.as_view(),
         name='update user dependent address'),
    path("GetFamilyByUserId/<int:UserId>/", GetFamilyByUserId.as_view()),
    path('FCMApi', FCMApi.as_view()),
    path('AnthropometricsPost/', AnthropometricsPost.as_view(), name='Bmicalculation'),
    path('AnthropometricsGetByUserId/<int:UserId>/', AnthropometricsGetByUserId().as_view(), name='Bmicalculation'),
    path('AnthropometricsUpdate/<int:id>/', AnthropometricsUpdate.as_view(), name='Bmicalculation'),
    path("AnthropometricsGetByFamilyMemberId/<int:FamilyId>/", AnthropometricsGetByFamilyById.as_view()),
    path('VitalsAPI/', VitalsAPI.as_view(), name='post vitals data'),
    path("GetVitalsByUserId/<int:UserId>/", GetVitalsByUserId.as_view()),
    path("GetVitalsByFamilyId/<int:FamilyId>/", GetVitalsByFamilyId.as_view()),
    path("UserVitalsUpdateApi/<int:Id>/", UserVitalsUpdateApi.as_view()),
    path("LabLevelPostAPI/", LabLevelPostAPI.as_view()),
    path("UserlablevelsUpdateApi/<int:Id>/", UserlablevelsUpdateApi.as_view()),
    path("GetLabLevelsByUserId/<int:UserId>/", GetLabLevelsByUserId.as_view()),
    path("GetLabLevelsByFamilyId/<int:FamilyId>/", GetLabLevelsByFamilyId.as_view()),
    path("AllergiesPost/", AllergiesPost.as_view()),
    path("AllergiesGetAll/",AllergiesGetApi.as_view()),
    path("AllergiesGetById/<int:UserId>/", GetAllergiesByUserId.as_view()),
    path("AllergiesGetByFamilyId/<int:FamilyId>/", GetAllergiesByFamilyId.as_view()),
    path("AllergiesUpdate/<int:id>",AllergiesUpdate.as_view()),
    path("MedicalsummaryGetByUserId/<int:UserId>",GetMedicalSummery.as_view()),
    path("MedicalsummaryGetByFamily/<int:FamilyId>",GetByFamilyidMedicalSummery.as_view()),
    path('GetAllMedicalSummary/',GetAllMedicalSummery.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
