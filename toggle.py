from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)  # adjust pin as needed
led = Pin(25, Pin.OUT)  # onboard LED

while True:
    # LED is on when button is NOT pressed
    led.value(button.value() != 1)
    time.sleep_ms(10)
