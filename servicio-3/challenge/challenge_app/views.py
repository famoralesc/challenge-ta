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

    parameters: dict = json.loads(request.body)

    if VERSION not in parameters or TIME_SEARCH not in parameters:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )
    version: int = parameters[VERSION]
    if version == 0:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )

    try:
        services.process(parameters[VERSION], parameters[TIME_SEARCH])
    except ValueError as e:
        return JsonResponse({"status": str(e)}, status=422)
    except Exception as e:
        return JsonResponse(
            {"status": f"Error: {{error}}".format(error=str(e))}, status=500
        )
    return JsonResponse({"status": "ok"}, status=200)


@csrf_exempt
def search(request) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"status": "Invalid HTTP method"}, status=405)

    parameters: dict = json.loads(request.body)

    if VERSION not in parameters:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )

    version: int = parameters["version"]
    type_parameter: str | None = parameters.get("type")
    sended: bool | None = parameters.get("sended")

    try:
        alerts = services.get_alerts_by_criteria(version, type_parameter, sended)
    except Exception as e:
        return JsonResponse(
            {"status": f"Error: {{error}}".format(error=str(e))}, status=500
        ) 

    return JsonResponse(alerts, status=200, safe=False)


def send(request):
    pass
