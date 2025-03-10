from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=5000)
    salary = models.CharField(max_length=15)
    salary_period = models.CharField(max_length=10,
                                     choices=[('hourly', 'Soatlik'), ('daily', 'Kunlik'), ('weekly', 'Haftalik'),
                                              ('monthly', 'Oylik')], blank=False, null=False)
    start_time = models.TimeField(default="08:00")
    end_time = models.TimeField(default="18:00")
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
