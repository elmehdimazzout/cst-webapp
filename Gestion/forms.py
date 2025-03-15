from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        CHOICES_sante = [('لا', 'لا'), ('نعم', 'نعم')]  

        widgets = {
            'nom_prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'date_entree': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'source_orientation': forms.TextInput(attrs={'class': 'form-control'}),

            'Cin': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'etat_matrimonial': forms.Select(attrs={'class': 'form-control'}),

            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nom_pere': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_mere': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'raison_direction': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'suite_couchage': forms.Select(attrs={'class': 'form-control'}),
            'chambre': forms.TextInput(attrs={'class': 'form-control'}),
            'date_sortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'raison_depart': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'son_compagnon': forms.TextInput(attrs={'class': 'form-control'}),
            'date_deces': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_deces': forms.TextInput(attrs={'class': 'form-control'}),

            # Handicaps et maladies
            'handicap_moteur': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'sourd_muet': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'deficience_visuelle': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'membres_amputes': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'maladie_mentale': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'diabete': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'pression_arterielle': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'tumeurs': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),
            'tuberculose': forms.Select(choices=CHOICES_sante, attrs={'class': 'form-select'}),

        }





