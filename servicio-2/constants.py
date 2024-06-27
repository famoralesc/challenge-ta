import os

TOPIC: str = "challenge/dispositivo/rx"
BROKER: str = "challenges-ta-mosquitto-1"
PORT: int = 1883

# INFLUX CONSTANTS
INFLUX_URL: str = "http://challenges-ta-influx-1:8086"
INFLUX_ORG: str = "tecnoandina"
INFLUX_BUCKET: str = "system"
INFLUX_USER: str = "admin"
INFLUX_PASSWORD: str = "admin"
INFLUX_MEASUREMENT: str = "dispositivos"
INFLUX_TOKEN: str = os.getenv("INFLUX_TOKEN", "default_token")
