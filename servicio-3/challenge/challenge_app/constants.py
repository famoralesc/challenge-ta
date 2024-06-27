import os

# INFLUX CONSTANTS
INFLUX_URL: str = "http://challenges-ta-influx-1:8086"
INFLUX_ORG: str = "tecnoandina"
INFLUX_BUCKET: str = "system"
INFLUX_MEASUREMENT: str = "dispositivos"
INFLUX_TOKEN: str = os.getenv("INFLUX_TOKEN", "default_token")


# API CONSTANTS
VERSION: str = "version"
TIME_SEARCH: str = "timeSearch"
BAJA: str = "BAJA"
MEDIA: str = "MEDIA"
ALTA: str = "ALTA"
