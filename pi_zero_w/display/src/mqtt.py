import time
import paho.mqtt.client as mqtt
import config

class Mqtt:
    def __init__(self):
        self.mqtt_client = mqtt.Client(client_id="pi_mqtt_client")

    def connect(self):
        # Configure automatic reconnect delays
        self.mqtt_client.reconnect_delay_set(min_delay=1, max_delay=60)

        connected = False
        while connected == False:
            try:
                self.mqtt_client.connect(config.mqtt_host, config.mqtt_port, keepalive=60)
                print("MQTT connected")
                connected = True
            except Exception as e:
                print(f"MQTT not connected {e}")
                time.sleep(3)

        # Start background network loop
        self.mqtt_client.loop_start()

    def subscribe(self, topics):
        for topic in topics:
            self.mqtt_client.subscribe(topic.name)

    def publish_message(self, topic, message):
        self.mqtt_client.publish(topic, message)

    def disconnect(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
