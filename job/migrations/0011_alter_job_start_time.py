# Generated by Django 5.1.5 on 2025-02-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_alter_job_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start_time',
            field=models.TimeField(default='08:00'),
        ),
    ]
