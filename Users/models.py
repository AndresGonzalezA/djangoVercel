# Users/models.py
from django.db import models

class Company(models.Model):
    id_company = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    logo = models.URLField()
    color = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models

class UserLoginAPI(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    celular = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
