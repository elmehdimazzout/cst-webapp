from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.user_login , name="login"),
    path("logout/", views.user_logout, name="logout"),

    path('', views.index, name='index'),  # الريسيسة  
    path('dashbord/', views.Dashbord, name='dashbord'), #لوحة تحكم

    path('list/', views.Patient_List, name='Patient_List'),  # عرض قائمة المرضى
    path('add/', views.Patient_Create, name='add_patient'),  # إضافة مريض جديد
    path('<int:id>/', views.Patient_Detail, name='patient_detail'),  # عرض تفاصيل مريض
    path('<int:id>/edit/', views.Patient_Update, name='edit_patient'),  # تعديل مريض
    path('<int:id>/delete/', views.Patient_Delete, name='delete_patient'),  # حذف مريض

    path('registredcd', views.Registre_dcd, name='Registre_dcd'),  # سجل الوفيات
    path('rgsortie/', views.Registre_Sortie, name='Registre_Sortie'),  # سجل المغادرون

    path('certificats', views.Certificats, name='Certificats'),  # شواهد ادارية
    path('uploaddata/', views.upload_excel, name='upload_excel'), #رفع جدول البيانات






 


]
