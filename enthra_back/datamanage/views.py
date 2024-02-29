# # En datamanage/views.py
# from django.http import JsonResponse
# from Users.models import Company
# from .models import DeviceData, Device
# import json
# from django.views.decorators.csrf import csrf_exempt

# # Acá manejamos los valores
# @csrf_exempt
# def get_company_device_info(request):
#     if request.method == 'POST':
#         try:
#             # Obtener datos del JSON enviado
#             json_data = json.loads(request.body.decode('utf-8'))
#             id_company = json_data.get('id_company', None)
#             id_device = json_data.get('id_device', None)

#             # Verificar que se hayan proporcionado los datos necesarios
#             if id_company is None or id_device is None:
#                 return JsonResponse({'error': 'Se requieren los campos id_company e id_device'}, status=400)

#             # Obtener información del modelo Company
#             company_info = Company.objects.filter(id_company=id_company).values('logo', 'color', 'name').first()

#             if not company_info:
#                 return JsonResponse({'error': 'La compañía no existe'}, status=404)

#             # Obtener información del modelo DeviceData
#             # Obtener información del modelo DeviceData
#             device_data_info = DeviceData.objects.filter(id_device=id_device).values('value', 'date')
#             device_data_list = list(device_data_info)

#             # Combinar la información obtenida
#             result = {
#                 'company_info': company_info,
#                 'device_data_info': device_data_list
#             }

#             return JsonResponse(result)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'JSON inválido'}, status=400)

#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# # Acá vamos a manajear los device name para listarlos en mi lista desplegable
# def get_device_names_by_company(request, id_company):
#     if request.method == 'GET':
#         # Obtener todos los nombres de dispositivos asociados al id_company
#         device_names = Device.objects.filter(id_company=id_company).values_list('name', flat=True)

#         # Convertir el queryset a una lista
#         device_names_list = list(device_names)

#         return JsonResponse({'device_names': device_names_list})

#     return JsonResponse({'error': 'Invalid request method'})
# En datamanage/views.py
from django.http import JsonResponse
from Users.models import Company
from .models import DeviceData, Device
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Acá manejamos los valores
@csrf_exempt
def get_company_device_info(request):
    if request.method == 'POST':
        try:
            # Obtener datos del JSON enviado
            json_data = json.loads(request.body.decode('utf-8'))
            id_company = json_data.get('id_company', None)
            device_name = json_data.get('device_name', None)
            start_date_str = json_data.get('start_date', None)
            end_date_str = json_data.get('end_date', None)

            # Verificar que se hayan proporcionado los datos necesarios
            if id_company is None or device_name is None or start_date_str is None or end_date_str is None:
                return JsonResponse({'error': 'Se requieren los campos id_company, device_name, start_date y end_date'}, status=400)
            
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

                # Obtener información del modelo DeviceData
            device_data_info = DeviceData.objects.filter(
                id_device__name=device_name,
                date__range=(start_date, end_date)
            ).values('value', 'date')
            print(device_data_info.query)

            device_data_list = list(device_data_info)
            # Combinar la información obtenida
            result = {
                'device_data_info': device_data_list
            }

            return JsonResponse(result)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Acá vamos a manejar los device names para listarlos en mi lista desplegable
def get_device_names_by_company(request, id_company):
    if request.method == 'GET':
        # Obtener todos los nombres de dispositivos asociados al id_company
        device_names = Device.objects.filter(id_company=id_company).values_list('name', flat=True)

        # Convertir el queryset a una lista
        device_names_list = list(device_names)

        return JsonResponse({'device_names': device_names_list})

    return JsonResponse({'error': 'Invalid request method'})
