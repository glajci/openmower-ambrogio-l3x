import network
import secrets
import utime

class wlan:

    def __init__(self, print_callback):
        self.wlan = network.WLAN(network.STA_IF)
        self.print_callback = print_callback

    def connect(self):
        sleep = 2
        while not self.wlan.isconnected():
            self.print_callback('WIFI connecting ...')
            self.wlan.active(False)
            self.wlan.disconnect()
            self.wlan.active(True)
            self.wlan.connect(secrets.ssid, secrets.password)
            utime.sleep(sleep)
            if sleep <= 5: sleep +=1
        self.print_callback('WIFI connected')

    def is_connected(self):
        is_connected = self.wlan.isconnected()
        if not is_connected: self.print_callback('WIFI disconnected')
        return is_connected