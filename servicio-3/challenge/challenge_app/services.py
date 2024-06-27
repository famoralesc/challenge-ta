from challenge_app.repository import influx as influx_repo
from challenge_app.constants import BAJA, MEDIA, ALTA
from challenge_app.models import Alerts
from django.db import IntegrityError


def get_data_from_influx(version: int, time_search: str) -> list[dict]:
    client = influx_repo.get_client()
    query = influx_repo.get_query(version, time_search)
    return influx_repo.get(client, query)


def validate_time_search_format(time_search: str) -> bool:
    rules = ["m" in time_search, "h" in time_search, "d" in time_search]
    return any(rules)


def get_alert_type(version: int, value: int) -> str:
    if version == 1:
        match value:
            case v if v > 200 and v < 500:
                return BAJA
            case v if v > 500 and v < 800:
                return MEDIA
            case v if v > 800:
                return ALTA
            case _:
                raise ValueError(f"No se puede determinar el type a partir del value {value}")
    if version == 2:
        match value:
            case v if v < 200:
                return BAJA
            case v if v < 500 and v > 200:
                return MEDIA
            case v if v < 800 and v > 500:
                return ALTA
            case _:
                raise ValueError(f"No se puede determinar el type a partir del value {value}")


def get_data_to_persist(version: int, data: list[dict]) -> list[dict]:
    if not data:
        return []
    
    response: list[dict]= []
    
    for record in data:
        response.append(
            {
                "datetime": record['time'],
                "type": get_alert_type(version, record['value']),
                "version": version,
                "value": record["value"]
            }
        )
    return response


def process(version: int, time_search: str) -> None:
    # VALIDATE PARAMETERS
    if not validate_time_search_format(time_search):
        raise ValueError("No se pudo procesar los párametros")

    if not time_search.startswith("-"):
        time_search = f"-{time_search}"

    # GET DATA FROM INFLUX
    influx_data = get_data_from_influx(version, time_search)    
    
    # INSERT DATA TO MYSQL
    data = get_data_to_persist(version, influx_data)

    for record in data:
        try:
            alert: Alerts = Alerts.objects.create(
                datetime = record['datetime'],
                type = record['type'],
                value = record['value'],
                version = record['version']
            )    
        except IntegrityError as e:
            pass
