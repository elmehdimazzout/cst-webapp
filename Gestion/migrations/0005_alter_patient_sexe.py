# Generated by Django 5.1.5 on 2025-03-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0004_alter_patient_adresse_alter_patient_date_naissance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'ذكر'), ('Femme', 'أنثى')], max_length=10),
        ),
    ]
