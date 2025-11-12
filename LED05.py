import RPi.GPIO as GPIO
from time import sleep

red_led = 17 #GPIO PIN
green_led = 27 #GPIO PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT) # set output
GPIO.setup(green_led, GPIO.OUT) # set output

try:
    while True:
        GPIO.output(red_led, 1)
        GPIO.output(green_led, 0)
        sleep(2)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)
        sleep(2) # delay
except KeyboardInterrupt:
    print("Exit program")
finally:
    # GPIO.cleanup() #initialize gpio setting
    GPIO.cleanup()