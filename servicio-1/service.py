import random
from time import sleep
from datetime import datetime
from paho.mqtt import client as mqtt_client
import constants as const

client_id = f"python-mqtt-{random.randint(0, 1000)}"


def connect_mqtt() -> mqtt_client.Client:
    print("Connecting...")

    def on_connect(client, userdata, flags, reason_code):
        if reason_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", reason_code)

    client = mqtt_client.Client(client_id=client_id)
    client.on_connect = on_connect
    client.connect(const.BROKER, const.PORT)
    return client


def publish(client: mqtt_client.Client) -> None:
    times = 0
    while True:
        times += 1
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

        msg = (
            "{\n"
            f"time: {date_time_str}\n,"
            f"value: {random.randint(0,1000)}\n,"
            f"version: {random.randint(0,2)}\n"
            "}"
        )

        result: mqtt_client.MQTTMessageInfo = client.publish(
            topic=const.TOPIC, payload=msg
        )
        status: int = result[0]
        if status == 0:
            print(f"Successful send {msg} to topic {const.TOPIC}")
        else:
            print(f"Error sending {msg} to topic {const.TOPIC}")
        sleep(const.TIME)
        if times == const.MAX_PUBLICATION_TIME:
            break


def main() -> None:
    print("Initializing...")
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == "__main__":
    main()
