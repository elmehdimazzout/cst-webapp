# Generated by Django 5.1.5 on 2025-03-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0015_delete_hospitalisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='etat_matrimonial',
            field=models.CharField(blank=True, choices=[('عازب', 'عازب'), ('متزوج', 'متزوج'), ('مطلق', 'مطلق'), ('أرمل', 'أرمل')], max_length=50, null=True),
        ),
    ]
