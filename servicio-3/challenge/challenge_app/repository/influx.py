from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.flux_table import TableList
from challenge_app.constants import *


def get_client() -> InfluxDBClient:
    client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
    return client


def get_query(version: int, time_search: str) -> str:
    query = f"""from(bucket: "{INFLUX_BUCKET}")
        |> range (start: {time_search})
        |> filter(fn: (r) => r["_measurement"] == "{INFLUX_MEASUREMENT}")
        |> filter(fn: (r) => r["version"] == "{version}")
    """
    return query


def get(client: InfluxDBClient, query: str) -> list[dict]:
    query_api: str = client.query_api()
    tables: TableList = query_api.query(query=query, org=INFLUX_ORG)
    result: list = []
    for table in tables:
        for record in table.records:
            result.append(
                {
                    "field": record.get_field(),
                    "start": record.get_start(),
                    "stop": record.get_stop(),
                    "value": record.get_value(),
                    "time": record.get_time(),
                    "row": record.get_row()
                }
            )
    return result
