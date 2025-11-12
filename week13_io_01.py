import RPi.GPIO as GPIO

# GPIO 설정
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def led_on(): 1 usage
    GPIO.output(LED_PIN, GPIO.LOW)