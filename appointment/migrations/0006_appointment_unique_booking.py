# Generated by Django 4.0.6 on 2022-08-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_remove_appointment_time_appointment_end_time_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(fields=('patient', 'doctor', 'date'), name='unique_booking'),
        ),
    ]
