from paho.mqtt import client as mqtt_client 
import constant as const
from time import sleep

def connect_mqtt() -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client: mqtt_client.Client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(const.BROKER, const.PORT)
    return client

def publish(client: mqtt_client.Client) -> None:
    while True:
        msg: str = f"message"
        result: mqtt_client.MQTTMessageInfo = client.publish(const.TOPIC, msg)
        status: int = result[0]
        if status == 0:
            print(f"Successful send {msg} to topic {const.TOPIC}")
        sleep(const.TIME)


def main():
    client = connect_mqtt()
    client.loop_start()
    client.publish(client)
    client.loop_stop()

if __name__ == "__main__":
    main()