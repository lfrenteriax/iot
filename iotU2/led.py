import name
import time
import RPi.GPIO as GPIO


# Pin definitions
led_pin = name.led_pin

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

state={'on':GPIO.HIGH,'off':GPIO.LOW}

def ledState(st):
    GPIO.output(led_pin, state[st])



