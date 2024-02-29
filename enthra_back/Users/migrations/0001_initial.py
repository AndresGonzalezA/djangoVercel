# Generated by Django 5.0.1 on 2024-01-22 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_company', models.AutoField(primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.URLField()),
                ('color', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginAPI',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.company')),
            ],
        ),
    ]
