# En datamanage/urls.py
from django.urls import path
from .views import get_company_device_info, get_device_names_by_company

urlpatterns = [
    path('get_company_device_info/', get_company_device_info, name='get_company_device_info'),
    path('get_device_names_by_company/<int:id_company>/', get_device_names_by_company, name='get_device_names_by_company'),
]
