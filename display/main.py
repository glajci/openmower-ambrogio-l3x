import time
import json

from gpiozero import Button
from mqtt import Mqtt
from openmower import Openmower
from display import Display
from menu import Menu


class App:
    def __init__(self):
        # Buttons (GPIO pins)
        # Adjust pin numbers for your wiring layout
        self.buttonUp = Button(19, pull_up=True)
        self.buttonDown = Button(16, pull_up=True)
        self.buttonEnter = Button(26, pull_up=True)
        self.buttonDock = Button(20, pull_up=False)
        self.buttonPlay = Button(21, pull_up=False)

        self.menu = Menu()
        self.display = Display()
        self.mqtt = Mqtt()
        self.mqtt.mqtt_client.on_connect = self.mqtt_on_connect
        self.mqtt.mqtt_client.on_disconnect = self.mqtt_on_disconnect
        self.mqtt.mqtt_client.on_message = self.mqtt_on_message
        self.init_display()
        self.mqtt.connect()

    def init_display(self):
        self.display.clear()
        self.display.draw_background()
        self.display.draw_splash("Openmower")
        self.display.draw_message("MQTT connecting")

    def mqtt_on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.mqtt.subscribe(Openmower.topics.get_all())
            self.display.draw_message("MQTT connected")
        else:
            print(f"Failed to connect, return code {rc}")
            self.init_display()
        
    def mqtt_on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection. Trying to reconnect...")
            self.init_display()
        else:
            print("Disconnected cleanly.")

    def mqtt_on_message(self, client, userdata, msg):
        topic = msg.topic
        message = msg.payload.decode()

        if topic == Openmower.topics.actions.name:
            Openmower.set_actions(json.loads(message))
            self.menu.set_actions()

        elif topic == Openmower.topics.robot_state.name:
            state = json.loads(message)
            if self.menu.is_active():
                return

            self.display.draw_mower_state(state["current_state"])
            self.display.draw_emergency(state["emergency"])
            self.display.draw_gps(
                state["pose"]["pos_accuracy"],
                state["gps_percentage"]
            )
            self.display.draw_battery(
                state["battery_percentage"],
                state["is_charging"]
            )

        elif topic == Openmower.topics.v_battery.name:
            if not self.menu.is_active():
                self.display.draw_battery_voltage(message)

    def mqtt_publish_message(self, topic, message):
        self.mqtt.publish_message(topic, message)

    def sleep(self):
        if not self.display.isAsleep:
            self.display.sleep()

    def wake(self):
        if self.display.isAsleep:
            self.display.wake()

def main():
    app = App()
    last_use = time.time()
    all_buttons_released = True

    while True:
        now = time.time()
        # Sleep after 60 seconds of inactivity
        # if now - last_use >= 60:
        #     app.sleep()

        button_pressed = False
        action = None

        if app.buttonPlay.is_pressed:
            print("play")
            button_pressed = True
            if all_buttons_released:
                if Openmower.actions.start_mowing.enabled:
                    action = Openmower.actions.start_mowing
                elif Openmower.actions.pause_mowing.enabled:
                    action = Openmower.actions.pause_mowing
                elif Openmower.actions.continue_mowing.enabled:
                    action = Openmower.actions.continue_mowing

        elif app.buttonDock.is_pressed:
            print("dock")
            button_pressed = True
            if all_buttons_released:
                action = Openmower.actions.abort_mowing

        elif app.buttonDown.is_pressed:
            print("down")
            button_pressed = True
            if all_buttons_released and not app.display.isAsleep:
                app.menu.go_down()
                app.display.draw_menu(
                    app.menu.current_item.title,
                    app.menu.current_item.subtitle,
                )

        elif app.buttonEnter.is_pressed:
            print("enter")
            button_pressed = True
            if all_buttons_released and not app.display.isAsleep:
                action = app.menu.current_item.action
                app.menu.enter()
                app.display.draw_menu(
                    app.menu.current_item.title,
                    app.menu.current_item.subtitle,
                )

        elif app.buttonUp.is_pressed:
            print("up")
            button_pressed = True
            if all_buttons_released and not app.display.isAsleep:
                app.menu.go_up()
                app.display.draw_menu(
                    app.menu.current_item.title,
                    app.menu.current_item.subtitle,
                )

        if all_buttons_released and button_pressed:
            last_use = time.time()
            if app.display.isAsleep:
                app.wake()
            elif action is not None and action.enabled:
                app.mqtt_publish_message("action", action.id)

        all_buttons_released = not button_pressed
        time.sleep(0.1)

if __name__ == "__main__":
    main()
