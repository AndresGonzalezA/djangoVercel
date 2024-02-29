from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserLoginAPI, Contact
from .serializers import UserLoginAPICreateSerializer, CompanySerializer, ContactSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime

class UserLoginAPIPostView(generics.CreateAPIView):
    queryset = UserLoginAPI.objects.all()
    serializer_class = UserLoginAPICreateSerializer

    def post(self, request, *args, **kwargs):
        # Obtener los datos del cuerpo de la solicitud
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # Buscar el usuario en la base de datos
        user_exists = UserLoginAPI.objects.filter(username=username, password=password).first()

        if user_exists:
            id_company = user_exists.id_company.id_company if user_exists.id_company else None

            # Devolver una respuesta exitosa con el id_company
            return Response({'detail': 'OK', 'id_company': id_company}, status=status.HTTP_200_OK)
        else:
            # Devolver una respuesta de error (puedes personalizar según tus necesidades)
            return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

class ContactFormView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)