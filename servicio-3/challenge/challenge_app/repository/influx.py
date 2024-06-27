from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from challenge_app.constants import *


def get_client() -> InfluxDBClient:
    client = InfluxDBClient(
        url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG
    )
    return client


def get_query(version: int, time: str) -> Point:
    query = f"""from(bucket: "{INFLUX_BUCKET}")
        |> range (start: {time})
        |> filter(fn: (r) => r["_measurement"] == "{INFLUX_MEASUREMENT}")
        |> filter(fn: (r) => r["version"] == "{version}")
    """
    return query

def get(
    client: InfluxDBClient, version: int, time: str) -> None:
    query_api = client.query_api()
    query = get_query(version, time)
    print("QUERY:::", query)
    tables = query_api.query(query=query, org=INFLUX_ORG)
    print("TABLES:::", tables)
    for table in tables:
        for record in table.records:
            print(record)
            print(f'Time: {record.get_time()}, Value: {record.get_value()}')

