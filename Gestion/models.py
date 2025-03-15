from django.db import models


class Patient(models.Model):
    nom_prenom = models.CharField(max_length=255, null=False, blank=False)
    sexe = models.CharField(max_length=10, choices=[('ذكر', 'ذكر'), ('أنثى', 'أنثى')], null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    source_orientation = models.CharField(max_length=255, null=False, blank=False)
    
    Cin = models.CharField(max_length=50, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=255, blank=True, null=True)
    etat_matrimonial_choices = [
        ('عازب', 'عازب'), 
        ('متزوج', 'متزوج'), 
        ('مطلق', 'مطلق'), 
        ('أرمل', 'أرمل')
    ]
    etat_matrimonial = models.CharField(max_length=50, choices=etat_matrimonial_choices, blank=True, null=True)

    adresse = models.TextField(blank=True, null=True)
    nom_pere = models.CharField(max_length=255, blank=True, null=True)
    nom_mere = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    raison_direction = models.TextField(blank=True, null=True) #سبب توجيه
    SUITE_COUCHAGE_CHOICES = [
        ('جناح الرجال', 'جناح الرجال'),
        ('جناح النساء', 'جناح النساء'),
        ('البنايات الجديدة رجال', 'البنايات الجديدة رجال'),
        ('العمارات', 'العمارات'),
    ]

    suite_couchage = models.CharField(
        max_length=100, 
        choices=SUITE_COUCHAGE_CHOICES, 
        blank=True, 
        null=True
    )#مكان المبيت
    chambre = models.CharField(max_length=50, blank=True, null=True)
    date_sortie = models.DateField(blank=True, null=True)
    raison_depart = models.TextField(blank=True, null=True)
    son_compagnon = models.CharField(max_length=255, blank=True, null=True)#مرافق للمغادر
    date_deces = models.DateField(blank=True, null=True)
    lieu_deces = models.CharField(max_length=255, blank=True, null=True)
    
    # Handicaps et maladies
    CHOICES = [
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    ]

    handicap_moteur = models.CharField(max_length=3, choices=CHOICES, default='لا')
    sourd_muet = models.CharField(max_length=3, choices=CHOICES, default='لا')
    deficience_visuelle = models.CharField(max_length=3, choices=CHOICES, default='لا')
    membres_amputes = models.CharField(max_length=3, choices=CHOICES, default='لا')
    maladie_mentale = models.CharField(max_length=3, choices=CHOICES, default='لا')
    diabete = models.CharField(max_length=3, choices=CHOICES, default='لا')
    pression_arterielle = models.CharField(max_length=3, choices=CHOICES, default='لا')
    tumeurs = models.CharField(max_length=3, choices=CHOICES, default='لا')
    tuberculose = models.CharField(max_length=3, choices=CHOICES, default='لا')
    
    def __str__(self):
        return f"{self.nom_prenom} ({self.id})"


