from mqtt import Mqtt
from openmower import Openmower
from display import Display
from menu import Menu
from machine import Pin
import json
import utime

class App:

    def __init__(self):
        self.buttonUp = Pin(2, Pin.IN, Pin.PULL_UP)
        self.buttonDown = Pin(3, Pin.IN, Pin.PULL_UP)
        self.buttonEnter = Pin(4, Pin.IN, Pin.PULL_UP)
        self.buttonDock = Pin(5, Pin.IN, Pin.PULL_DOWN)
        self.buttonPlay = Pin(6, Pin.IN, Pin.PULL_DOWN)
        self.buttonUp.value(1)
        self.buttonDown.value(1)        
        self.buttonEnter.value(1)
        self.menu = Menu()
        self.display = Display() 
        self.mqtt = Mqtt(self.mqtt_message_received, Openmower.topics.get_all(), self.display.draw_print_message)  
        self.init_display()

    def init_display(self):
        self.display.clear()
        self.display.draw_background()
        self.display.draw_splash()
        self.mqtt.connect()

    def mqtt_message_received(self, topic, message):   
        if topic == Openmower.topics.actions.b_name:
            Openmower.set_actions(json.loads(message))
            self.menu.set_actions()
        elif topic == Openmower.topics.robot_state.b_name:
            state = json.loads(message)
            if self.menu.is_active():
                return
            self.display.draw_mower_state(state['current_state'])
            self.display.draw_emergency(state['emergency'])
            self.display.draw_gps(state['pose']['pos_accuracy'], state['gps_percentage'])
            self.display.draw_battery(state['battery_percentage'], state['is_charging'])
        elif topic == Openmower.topics.v_battery.b_name:
            if self.menu.is_active():
                return
            self.display.draw_battery_voltage(message)

    def mqtt_publish_message(self, topic, message):
        self.mqtt.publish_message(topic, message)
        
    def sleep(self):
        if not self.display.isAsleep:
            self.display.sleep()
    
    def wake(self):
        if self.display.isAsleep:
            self.display.wake()

app = App()
last_use = utime.ticks_ms()
last_connection_check = utime.ticks_ms()
all_buttons_released = True

while True:    
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_use) >= 60000:
        app.sleep()

    button_pressed = False
    action = None

    if app.buttonPlay.value() == 1:
        print('play')
        button_pressed = True
        if all_buttons_released:
            if Openmower.actions.start_mowing.enabled:
                action = Openmower.actions.start_mowing
            elif Openmower.actions.pause_mowing.enabled:
                action = Openmower.actions.pause_mowing
            elif Openmower.actions.continue_mowing.enabled:
                action = Openmower.actions.continue_mowing

    elif app.buttonDock.value() == 1:
        print('dock')
        button_pressed = True              
        if all_buttons_released: 
            action = Openmower.actions.abort_mowing

    elif app.buttonDown.value() == 0:
        print('down')
        button_pressed = True
        if all_buttons_released and not app.display.isAsleep:
            app.menu.go_down()
            app.display.draw_menu(app.menu.current_item.title, app.menu.current_item.subtitle)

    elif app.buttonEnter.value() == 0:
        print('enter')
        button_pressed = True
        if all_buttons_released and not app.display.isAsleep:
            action = app.menu.current_item.action
            app.menu.enter()
            app.display.draw_menu(app.menu.current_item.title, app.menu.current_item.subtitle)

    elif app.buttonUp.value() == 0:
        print('up')
        button_pressed = True
        if all_buttons_released and not app.display.isAsleep:
            app.menu.go_up()
            app.display.draw_menu(app.menu.current_item.title, app.menu.current_item.subtitle)

    if all_buttons_released and button_pressed:
        last_use = utime.ticks_ms()
        if app.display.isAsleep:
            app.wake()
        elif action != None and action.enabled:
            app.mqtt_publish_message("action", action.id)

    all_buttons_released = not button_pressed

    if utime.ticks_diff(now, last_connection_check) >= 2000:
        if not app.mqtt.is_connected():
            app.init_display()
        last_connection_check = utime.ticks_ms()

    try:
        app.mqtt.check_message()
    except:
        utime.sleep(2)

    utime.sleep(0.1)
