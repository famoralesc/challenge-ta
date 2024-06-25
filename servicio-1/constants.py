TIME: int = 1
TOPIC: str = "challenge/dispositivo/rx"
BROKER: str = "challenges-ta-mosquitto-1"
PORT: int = 1883
MAX_PUBLICATION_TIME: int = 5
MESSAGE_TEMPLATE = """{{
"time": "{time}",
"value": {value},"
"version: {version}"
}}"""
