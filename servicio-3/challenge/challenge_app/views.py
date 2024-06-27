from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from challenge_app.constants import VERSION, TIME_SEARCH
from services import process as service_process

import json


# HOME
def index(request):
    pass


# APIS
@csrf_exempt
def process(request) -> JsonResponse:
    print(type(request))
    if request.method != 'POST':
        return JsonResponse({'status': "Invalid HTTP method"}, status=405)

    data = json.loads(request.body)
    
    if VERSION not in data or TIME_SEARCH not in data:
        return JsonResponse({"status": "No se pudo procesar los párametros"}, status=422)
    
    try:
        result = service_process(data)
    except ValueError as e:
        return JsonResponse({"status": e}, status=422)
    return JsonResponse({}, status=200)

def search(request):
    pass

def send(request):
    pass