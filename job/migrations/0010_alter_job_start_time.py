# Generated by Django 4.2.5 on 2023-12-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_address_alter_job_name_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start_time',
            field=models.TimeField(default='8:00'),
        ),
    ]
