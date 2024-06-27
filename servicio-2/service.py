import random
import json
from paho.mqtt import client as mqtt_client
import constants as const
from repository import influx

client_id = f"python-mqtt-{random.randint(0, 1000)}"


def connect_mqtt() -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=client_id)
    client.on_connect = on_connect
    client.connect(const.BROKER, const.PORT)
    return client


def subscribe(client: mqtt_client.Client) -> None:
    influx_client = influx.get_client()

    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        data = json.loads(payload)

        if influx_client.health().status == "pass":
            influx.write(
                client=influx_client,
                version=data["version"],
                time=data["time"],
                value=data["value"],
            )
        else:
            print("There is a problem with influx's health connection")

    client.subscribe(topic=const.TOPIC)
    client.on_message = on_message


def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    main()
