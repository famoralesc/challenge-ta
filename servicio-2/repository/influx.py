from datetime import datetime
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from constants import *


def get_client() -> InfluxDBClient:
    client = InfluxDBClient(
        url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG
    )
    return client


def get_point(version: int, time: str, value: int) -> Point:
    point = (
        Point(INFLUX_MEASUREMENT)
        .tag("version", version)
        .field("time", time)
        .field("value", value)
        .time(datetime.now())
    )
    return point


def write(
    client: InfluxDBClient, version: int, time: str, value: int
) -> None:
    point = get_point(version, time, value)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
