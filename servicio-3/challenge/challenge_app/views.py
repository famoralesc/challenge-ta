from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from challenge_app.constants import VERSION, TIME_SEARCH
from challenge_app import services
import json


# HOME
def index(request):
    pass


# APIS
@csrf_exempt
def process(request) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"status": "Invalid HTTP method"}, status=405)

    data = json.loads(request.body)

    if VERSION not in data or TIME_SEARCH not in data:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )
    version = data[VERSION]
    if version == 0:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )
    
    try:
        services.process(data[VERSION], data[TIME_SEARCH])
    except ValueError as e:
        return JsonResponse({"status": str(e)}, status=422)
    except Exception as e:
        return JsonResponse({"status": f"Error: {{error}}".format(error=str(e))}, status=500)
    return JsonResponse({"status": "ok"}, status=200)


def search(request):
    pass


def send(request):
    pass
