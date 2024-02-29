# Users/urls.py
from django.urls import path
from .views import UserLoginAPIPostView, index, ContactFormView

urlpatterns = [
    # Ruta para la vista de verificación de usuario
    path('', index),
    path('api/users/verify/', UserLoginAPIPostView.as_view(), name='user-verify'),
    path('home/', index, name='home'),
    path('contact/', ContactFormView.as_view(), name='contact-form'),
]
