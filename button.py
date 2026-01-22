import RPi.GPIO as GPIO
import requests
import time

BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        requests.get("http://localhost:5000/order")
        print("Button gedrückt → Bestellung ausgelöst!")
        time.sleep(1)
