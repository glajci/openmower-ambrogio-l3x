import config
import time
#import upip
from umqtt.simple import MQTTClient
from wlan import wlan

class Mqtt:
    
    def __init__(self, message_received_callback, topics, print_callback):
        self.message_received_callback = message_received_callback
        self.topics = topics
        self.print_callback = print_callback
        self.wlan = wlan(print_callback)

        #In case your UF2 does not include micropython-umqtt.simple - this only needs to be run once.
        #upip.install("micropython-umqtt.simple")

        self.mqtt_client = MQTTClient("pi_mqtt_client", config.mqtt_host, config.mqtt_port)
        self.mqtt_client.set_callback(self.subscription_callback)


    def connect(self):
        if not self.is_connected():
            self.wlan.connect()

        connected = False
        while connected == False:
            try:
                self.mqtt_client.connect()
                connected = True
                self.print_callback('MQTT connected')
            except:
                self.print_callback('MQTT connecting ...')
                time.sleep(3)
        
        for topic in self.topics:
            self.mqtt_client.subscribe(topic.name)

    def subscription_callback(self, topic, message):
        # print(f'Topic {topic} received message {message}')
        self.message_received_callback(topic, message)

    def check_message(self):
        self.mqtt_client.check_msg()
        
    def publish_message(self, topic, message):
        self.mqtt_client.publish(topic, message)

    def is_connected(self):
        return self.wlan.is_connected() 
    

