TIME: int = 60
TOPIC: str = "challenge/dispositivo/rx"
BROKER: str = "challenges-ta-mosquitto-1"
PORT: int = 1883
MAX_PUBLICATION_TIME: int = 100
MESSAGE_TEMPLATE = """{{
"time": "{time}",
"value": {value},
"version": {version}
}}"""
