from django.urls import path,include
from patients.views import list_patients,patient_detail,add_patient
from doctors.views import list_doctors,doctor_detail
from rooms.views import list_rooms,room_detail,add_room


urlpatterns = [
    path('patient-list/',list_patients,name='List_Patients'),
    path('patient-list/<int:pk>',patient_detail,name='Patient_Detail'),
    path('doctor-list/',list_doctors,name='List_Doctors'),
    path('doctor-list/<int:pk>',doctor_detail,name='Doctor_Detail'),
    path('room-list/',list_rooms,name='List_Rooms'),
    path('room-list/<int:pk>',room_detail,name='Room_Detail'),
    path('create-room',add_room,name='Create_Room'),
    path('add-patient',add_patient,name='Add_Patient')
]
