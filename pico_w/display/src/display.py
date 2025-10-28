from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

class Display:

    def __init__(self):
        self.i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        self.lcd = I2cLcd(self.i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
        self.define_custom_characters()
        self.clear()
        self.emergency = False

    def clear(self):
        self.isAsleep = True
        self.lcd.clear()   

    def draw_background(self):
        self.isAsleep = False

    def draw_splash(self):
        self.lcd.move_to(0,0)
        self.lcd.putstr("Openmower" + " " * (16 - len("Openmower")))

    def draw_mower_state(self, state):
        self.lcd.move_to(0,0)
        self.lcd.putstr(state + " " * (15 - len(state)))

    def draw_emergency(self, emergency: bool):     
        self.lcd.move_to(15,0)
        if emergency:
            self.lcd.putchar(chr(0))
        else:
            self.lcd.putstr(' ')

    def draw_gps(self, accuracy, percentage):
        self.lcd.move_to(0,1)
        if accuracy <= 0.05:
            self.lcd.putchar(chr(7))
        elif accuracy <= 0.2:
            self.lcd.putchar(chr(6))
        else:
            self.lcd.putchar(chr(5))

        if accuracy > 1:
            accuracy_formatted = f'{str(round(accuracy, 1))}m'
        else:
            accuracy_formatted = f'{str(round(accuracy, 3) * 100)}cm'

        self.lcd.move_to(1,1)
        self.lcd.putstr(accuracy_formatted + " " * (7 - len(accuracy_formatted)))

    def draw_battery(self, percentage, is_charging):
        char_index = int(percentage * 2) + 1

        if is_charging:
            char_index = 4

        self.lcd.move_to(15,1)
        self.lcd.putchar(chr(char_index))

    def draw_battery_voltage(self, voltage):
        voltage_formatted = f'{round(float(voltage.decode()), 1)}V'
        self.lcd.move_to(8,1)
        self.lcd.putstr(" " * (7 - len(voltage_formatted)) + voltage_formatted)

    def draw_menu(self, title, subtitle):
        if title == None: return
        self.lcd.move_to(0,0)
        self.lcd.putstr(title + " " * (16 - len(title)))
        self.lcd.move_to(0,1)
        self.lcd.putstr(subtitle + " " * (16 - len(subtitle)))

    def draw_print_message(self, message):
        self.lcd.move_to(0,1)
        self.lcd.putstr((message[:16]) + " " * (16 - len(message[:16])))
                
    def sleep(self):
        self.lcd.backlight_off()
        self.isAsleep = True     
        
    def wake(self):
        self.lcd.backlight_on()
        self.isAsleep = False

    def define_custom_characters(self):
    
        # how to create customcharacters https://maxpromer.github.io/LCD-Character-Creator/ 
  
        #emergency      
        self.lcd.custom_char(0, bytearray([
            0xe,0xe,0xe,0xe,0xe,0x0,0xe,0xe
        ]))

        #battery empty
        self.lcd.custom_char(1, bytearray([
            0xe,0x11,0x11,0x11,0x11,0x11,0x1f,0x00
        ]))
  
        #battery 50%
        self.lcd.custom_char(2, bytearray([
            0xe,0x11,0x11,0x11,0x1f,0x1f,0x1f,0x00
        ]))
  
        #battery 100%
        self.lcd.custom_char(3, bytearray([
            0xe,0x1f,0x1f,0x1f,0x1f,0x1f,0x1f,0x00
        ]))
  
        #battery charging
        self.lcd.custom_char(4, bytearray([
            0xe,0x1b,0x17,0x11,0x1d,0x1b,0x1f,0x00
        ]))

        #gps no rtk      
        self.lcd.custom_char(5, bytearray([
            0x0,0xe,0x19,0x15,0x13,0xe,0x0,0x0
        ]))

        #gps rtk float      
        self.lcd.custom_char(6, bytearray([
            0x0,0xe,0x11,0x11,0x11,0xe,0x0,0x0
        ]))

        #gps rtk fixed    
        self.lcd.custom_char(7, bytearray([
            0x0,0xe,0x1f,0x1b,0x1f,0xe,0x0,0x0
        ]))