# Generated by Django 5.1.5 on 2025-03-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0010_remove_patient_handicap_gras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='deficience_visuelle',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diabete',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='handicap_moteur',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='maladie_mentale',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='membres_amputes',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pression_arterielle',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sourd_muet',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tuberculose',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tumeurs',
            field=models.CharField(choices=[('نعم', 'نعم'), ('لا', 'لا')], default='لا', max_length=3),
        ),
    ]
