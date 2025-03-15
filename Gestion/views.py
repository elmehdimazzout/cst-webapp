from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required ,permission_required
from .models import Patient
from .forms import PatientForm  # تأكد من إنشاء الفورم
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from datetime import date, timedelta
from collections import Counter
from django.urls import reverse_lazy
from django.http import JsonResponse







#صفحة الدخول
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")  # حول المستخدم للصفحة الرئيسية
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة!")
    return render(request, "login.html")

#الخروج
def user_logout(request):
    logout(request)
    return redirect("login")  # رجع المستخدم لصفحة تسجيل الدخول بعد تسجيل الخروج

#لوحة تحكم واحصاءات
@login_required
def Dashbord(request):
    # حساب عدد الذكور والإناث من قاعدة البيانات
    men_count = Patient.objects.filter(sexe="ذكر").count()
    women_count = Patient.objects.filter(sexe="أنثى").count()
    total_count = men_count + women_count  #  المجموع 

    today = date.today()
    sixty_years_ago = today - timedelta(days=60*365)  # تقدير 60 سنة بالأيام
    seniors_count = Patient.objects.filter(date_naissance__lte=sixty_years_ago).count()

    stats = {
        'women_count': women_count,
        'men_count': men_count,
        'total_count': total_count,
        'seniors_count': seniors_count, #العجزة 
 
    }
    return render(request, 'pages/Dashbord.html', stats)


#الصفحة الرئيسية
@login_required
def index(request):
    return render(request, 'index.html')

# عرض قائمة المرضى
@login_required
def Patient_List(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

# إضافة مريض جديد
@login_required
def Patient_Create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()  # حفظ المريض واسترجاع الكائن
            return redirect('patient_detail', id=patient.id)
    else:
        form = PatientForm()
    return render(request, 'patients/form.html', {'form': form})

# عرض تفاصيل مريض
@login_required
def Patient_Detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/detail.html', {'patient': patient})

# تعديل مريض
@login_required
def Patient_Update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', id=patient.id)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/form.html', {'form': form})

# حذف مريض
@login_required
def Patient_Delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    
    if request.method == 'POST':
        patient.delete()
        return JsonResponse({'success': True})  # ✅ تأكيد الحذف
        
    return JsonResponse({'success': False, 'error': 'طلب غير صالح'}, status=400)
    
#الوفيات
@login_required
def Registre_dcd(request):
    deceased_patients = Patient.objects.filter(date_deces__isnull=False)  # جلب غير المرضى المتوفين
    return render(request, 'patients/Registre_dcd.html', {'patients': deceased_patients})
#المغادرون
@login_required
def Registre_Sortie(request):
    sortie_patients = Patient.objects.filter(date_sortie__isnull=False)  # جلب المرضى الذين غادروا
    return render(request, 'patients/Registre_Sortie.html', {'patients': sortie_patients})


@login_required #شواهد ادارية
def Certificats(request):
    return render(request, 'patients/Certificats.html')

#تحميل بيانات من اكسل الى قاعدة البيانات
import pandas as pd
@login_required
def upload_excel(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file, engine='openpyxl')  # قراءة الملف

            # تعويض القيم الفارغة في الأمراض بـ "لا"
            maladie_columns = [
                'handicap_moteur', 'sourd_muet', 'deficience_visuelle', 
                'membres_amputes', 'maladie_mentale', 'diabete', 
                'pression_arterielle', 'tumeurs', 'tuberculose'
            ]
            for col in maladie_columns:
                df[col] = df[col].fillna("لا")

            # تعويض القيم الفارغة الأخرى بـ None
            df = df.where(pd.notna(df), None)

            # ✅ تعويض `source_orientation` بالقيمة الافتراضية إذا كان فارغًا
            df['source_orientation'] = df['source_orientation'].fillna("غير معروف")

            # ✅ تحويل التواريخ إلى قيم صحيحة أو None إذا كانت غير صالحة
            date_columns = ['date_entree', 'date_naissance', 'date_sortie', 'date_deces']
            for col in date_columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')  # يحول القيم غير الصالحة إلى NaT
                df[col] = df[col].dt.date  # يحتفظ فقط بالتاريخ بدون التوقيت

            for index, row in df.iterrows():
                Patient.objects.create(
                    nom_prenom=row.get('nom_prenom', ''),
                    sexe=row.get('sexe', 'غير محدد'),
                    date_entree=row.get('date_entree') if pd.notna(row.get('date_entree')) else None,
                    source_orientation=row.get('source_orientation', 'غير معروف'),  # ✅ حل نهائي
                    Cin=row.get('Cin', ''),
                    date_naissance=row.get('date_naissance') if pd.notna(row.get('date_naissance')) else None,
                    lieu_naissance=row.get('lieu_naissance', ''),
                    etat_matrimonial=row.get('etat_matrimonial', 'مجهول'),
                    adresse=row.get('adresse', 'مجهول'),
                    nom_pere=row.get('nom_pere', 'مجهول'),
                    nom_mere=row.get('nom_mere', 'مجهول'),
                    telephone=row.get('telephone', 'مجهول'),
                    raison_direction=row.get('raison_direction', 'مجهول'),
                    suite_couchage=row.get('suite_couchage', 'مجهول'),
                    chambre=row.get('chambre', 'مجهول'),
                    date_sortie=row.get('date_sortie') if pd.notna(row.get('date_sortie')) else None,
                    raison_depart=row.get('raison_depart', ''),
                    son_compagnon=row.get('son_compagnon', ''),
                    date_deces=row.get('date_deces') if pd.notna(row.get('date_deces')) else None,
                    lieu_deces=row.get('lieu_deces', ''),
                    handicap_moteur=row.get('handicap_moteur', 'لا'),
                    sourd_muet=row.get('sourd_muet', 'لا'),
                    deficience_visuelle=row.get('deficience_visuelle', 'لا'),
                    membres_amputes=row.get('membres_amputes', 'لا'),
                    maladie_mentale=row.get('maladie_mentale', 'لا'),
                    diabete=row.get('diabete', 'لا'),
                    pression_arterielle=row.get('pression_arterielle', 'لا'),
                    tumeurs=row.get('tumeurs', 'لا'),
                    tuberculose=row.get('tuberculose', 'لا'),
                )

            messages.success(request, "تم رفع البيانات بنجاح!")
        except Exception as e:
            messages.error(request, f"خطأ أثناء معالجة الملف: {e}")

        return redirect('upload_excel')

    return render(request, 'pages/upload_excel.html')


