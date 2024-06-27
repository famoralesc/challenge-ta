from challenge_app.repository import influx as influx_repo
from challenge_app.constants import VERSION, TIME_SEARCH

def get_data_from_influx(version: int, time_search: str) -> dict:
    client = influx_repo.get_client()
    raw_data = influx_repo.get(client, version, time_search)
    # PROCESS RAW_DATA 
    return {}

def validate_time_search_format(time_search: str) -> bool:
    rules = [
        "m" in time_search,
        "h" in time_search,
        "d" in time_search
    ]
    return any(rules)


def process(parameters: dict) -> dict:
    # VALIDATE PARAMETERS
    version = parameters[VERSION]
    time_search = parameters[TIME_SEARCH]

    if not validate_time_search_format(time_search):
        raise ValueError("No se pudo procesar los párametros")

    # GET DATA FROM INFLUX
    influx_data = get_data_from_influx(version, time_search)    
    # INSERT DATA TO MYSQL
    
    return {}