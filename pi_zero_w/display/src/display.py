import smbus2
import time

# Adjust this if needed — check with `sudo i2cdetect -y 1`
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# LCD constants
LCD_CHR = 1
LCD_CMD = 0
LCD_BACKLIGHT = 0x08  # 0x08 = ON, 0x00 = OFF
ENABLE = 0b00000100

E_PULSE = 0.0005
E_DELAY = 0.0005

class Display:
    def __init__(self):
        self.bus = smbus2.SMBus(1)
        self.backlight_state = LCD_BACKLIGHT
        self.emergency = False
        self.isAsleep = False

        self.lcd_init()
        self.define_custom_characters()
        self.clear()

    # ---------- Low-level LCD control ----------
    def lcd_strobe(self, data):
        self.bus.write_byte(I2C_ADDR, data | ENABLE | self.backlight_state)
        time.sleep(E_PULSE)
        self.bus.write_byte(I2C_ADDR, ((data & ~ENABLE) | self.backlight_state))
        time.sleep(E_DELAY)

    def lcd_write_four_bits(self, data):
        self.bus.write_byte(I2C_ADDR, data | self.backlight_state)
        self.lcd_strobe(data)

    def lcd_write(self, cmd, mode=0):
        high = mode | (cmd & 0xF0)
        low = mode | ((cmd << 4) & 0xF0)
        self.lcd_write_four_bits(high)
        self.lcd_write_four_bits(low)

    def lcd_init(self):
        self.lcd_write(0x33, LCD_CMD)
        self.lcd_write(0x32, LCD_CMD)
        self.lcd_write(0x06, LCD_CMD)
        self.lcd_write(0x0C, LCD_CMD)
        self.lcd_write(0x28, LCD_CMD)
        self.lcd_write(0x01, LCD_CMD)
        time.sleep(E_DELAY)

    def clear(self):
        self.lcd_write(0x01, LCD_CMD)
        time.sleep(E_DELAY)
        self.isAsleep = True

    def move_to(self, col, row):
        row_offsets = [0x80, 0xC0]
        self.lcd_write(row_offsets[row] + col, LCD_CMD)

    def putstr(self, message):
        for char in message:
            self.lcd_write(ord(char), LCD_CHR)

    def putchar(self, ch):
        self.lcd_write(ord(ch), LCD_CHR)

    # ---------- High-level Drawing ----------
    def draw_background(self):
        self.isAsleep = False

    def draw_splash(self, message):
        self.move_to(0, 0)
        self.putstr(message.ljust(16))

    def draw_mower_state(self, state):
        self.move_to(0, 0)
        self.putstr(state.ljust(15))

    def draw_emergency(self, emergency: bool):
        self.move_to(15, 0)
        if emergency:
            self.putchar(chr(0))  # custom char 0
        else:
            self.putstr(" ")

    def draw_gps(self, accuracy, percentage):
        self.move_to(0, 1)
        if accuracy <= 0.05:
            self.putchar(chr(7))
        elif accuracy <= 0.2:
            self.putchar(chr(6))
        else:
            self.putchar(chr(5))

        if accuracy > 1:
            accuracy_formatted = f"{round(accuracy, 1)}m"
        else:
            accuracy_formatted = f"{round(accuracy * 100, 1)}cm"

        self.move_to(1, 1)
        self.putstr(accuracy_formatted.ljust(7))

    def draw_battery(self, percentage, is_charging):
        char_index = int(percentage * 2) + 1
        if is_charging:
            char_index = 4

        self.move_to(15, 1)
        self.putchar(chr(char_index))

    def draw_battery_voltage(self, voltage):
        voltage_value = float(voltage.decode()) if isinstance(voltage, bytes) else float(voltage)
        voltage_formatted = f"{round(voltage_value, 1)}V"
        self.move_to(8, 1)
        self.putstr(voltage_formatted.rjust(7))

    def draw_menu(self, title, subtitle):
        if title is None:
            return
        self.move_to(0, 0)
        self.putstr(title.ljust(16))
        self.move_to(0, 1)
        self.putstr(subtitle.ljust(16))

    def draw_message(self, message):
        self.move_to(0, 1)
        msg = message[:16]
        self.putstr(msg.ljust(16))

    def sleep(self):
        self.backlight_state = 0x00
        self.bus.write_byte(I2C_ADDR, self.backlight_state)
        self.isAsleep = True

    def wake(self):
        self.backlight_state = LCD_BACKLIGHT
        self.bus.write_byte(I2C_ADDR, self.backlight_state)
        self.isAsleep = False

    # ---------- Custom Characters ----------
    def define_custom_characters(self):
        # emergency
        self.create_char(0, [0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x00, 0x0E, 0x0E])
        # battery empty
        self.create_char(1, [0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1F, 0x00])
        # battery 50%
        self.create_char(2, [0x0E, 0x11, 0x11, 0x11, 0x1F, 0x1F, 0x1F, 0x00])
        # battery full
        self.create_char(3, [0x0E, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x00])
        # battery charging
        self.create_char(4, [0x0E, 0x1B, 0x17, 0x11, 0x1D, 0x1B, 0x1F, 0x00])
        # gps no rtk
        self.create_char(5, [0x00, 0x0E, 0x19, 0x15, 0x13, 0x0E, 0x00, 0x00])
        # gps rtk float
        self.create_char(6, [0x00, 0x0E, 0x11, 0x11, 0x11, 0x0E, 0x00, 0x00])
        # gps rtk fixed
        self.create_char(7, [0x00, 0x0E, 0x1F, 0x1B, 0x1F, 0x0E, 0x00, 0x00])

    def create_char(self, location, charmap):
        """Write custom char to CGRAM"""
        location &= 0x7  # Only 8 slots (0–7)
        self.lcd_write(0x40 | (location << 3), LCD_CMD)
        for byte in charmap:
            self.lcd_write(byte, LCD_CHR)
