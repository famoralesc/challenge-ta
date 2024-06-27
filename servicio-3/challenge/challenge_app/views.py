from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from challenge_app.constants import VERSION, TIME_SEARCH
from challenge_app import services
import json

BASE_HTML_ROUTE = "alerts"


# HOME
def index(request):
    html_route = "index.html"
    return render(request, f"{BASE_HTML_ROUTE}/{html_route}", {})


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
    version: int = int(parameters[VERSION])
    if version == 0:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )

    try:
        services.process(version, parameters[TIME_SEARCH])
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

    version: int = int(parameters[VERSION])
    type_parameter: str | None = parameters.get("type")
    sended: bool | None = parameters.get("sended")

    try:
        alerts = services.get_alerts_by_criteria(version, type_parameter, sended)
    except Exception as e:
        return JsonResponse(
            {"status": f"Error: {{error}}".format(error=str(e))}, status=500
        )

    return JsonResponse(alerts, status=200, safe=False)


@csrf_exempt
def send(request):
    if request.method != "POST":
        return JsonResponse({"status": "Invalid HTTP method"}, status=405)

    parameters: dict = json.loads(request.body)

    if VERSION not in parameters or "type" not in parameters:
        return JsonResponse(
            {"status": "No se pudo procesar los párametros"}, status=422
        )
    version: int = int(parameters[VERSION])
    type_parameter: str = parameters.get("type")

    try:
        services.send_alerts(version, type_parameter)
    except Exception as e:
        return JsonResponse(
            {"status": f"Error: {{error}}".format(error=str(e))}, status=500
        )
    return JsonResponse({"status": "ok"}, status=200)
