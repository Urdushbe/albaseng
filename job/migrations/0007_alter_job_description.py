# Generated by Django 4.2.5 on 2023-09-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
