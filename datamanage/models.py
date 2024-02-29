from django.db import models
from Users.models import Company

class Device(models.Model):
    id_device = models.AutoField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='id_company')
    name = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DeviceData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    id_device = models.ForeignKey(Device, on_delete=models.CASCADE, db_column='id_device')

    def __str__(self):
        return f"{self.id_device.name} - {self.date}"

class Ping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.date}"