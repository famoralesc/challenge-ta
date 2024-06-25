from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from constants import *


def initialize() -> InfluxDBClient:
    client = InfluxDBClient(
        url=INFLUX_URL,
        username=INFLUX_USER,
        password=INFLUX_PASSWORD,
        auth_basic=True
    )
    return client


def get_point(version: int, time: str, value: int) -> Point:
    point = (
        Point(INFLUX_MEASUREMENT)
        .tag("version", version)
        .field("time", time)
        .field("value", value)
    )
    return point


def write_to_influx(
    client: InfluxDBClient, version: int, time: str, value: int
) -> None:
    point = get_point(version, time, value)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
