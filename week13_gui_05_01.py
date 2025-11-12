from tkinter import *
from gpiozero import LED

# LED 핀 번호 설정

# 레이블 생성 (초기 배경: 회색)
status_label = Label(win,
        text="LED OFF", bg="gray", fg="white", font=("Arial", 18), width=12, height=2)
status_label.pack(pady=20)

def toggle_led(): 1 usage
    global led_on
    if led_on:
        led.off()
        status_label.config(text="LED OFF", bg="gray")
        led_button.config(text="LED ON")
        led_on = False
    else:
        led.on()
        status_label.config(text="LED ON", bg="gray")
        led_button.config(text="LED OFF")
        led_on = True
        
    def on_exit(): 1 usage
    red_led