# Generated by Django 4.2.5 on 2023-10-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='telegram',
            field=models.CharField(blank=True, default="to'ldirilmagan!", max_length=500, null=True),
        ),
    ]
