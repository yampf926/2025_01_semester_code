# led 추가 버전
from tkinter import *
from gpiozero import LED

# LED 핀 번호 설정 (RED 18번, GREEN 17번)
red_led = LED(18)
green_led = LED(17)

# tkinter 윈도우 생성
win = Tk()
win.title("LED 제어 GUI")
win.geometry("300x600")

# LED를 저장활 변수
red_led_on = False
green_led_on = False

# 레이블 생성 (초기 배경: 회색)
status_label = Label(win, text="RED LED OFF", bg="gray", fg="white", font=("Arial", 18), width=12, height=2)
status_label.pack(pady=20)
status_label = Label(win, text="GREEN LED OFF", bg="gray", fg="white", font=("Arial", 18), width=12, height=2)
status_label.pack(pady=20)

def toggle_red_led(): 1 usage
    global red_led_on
    if red_led_on:
        led.off()
        red_status_label.config(text="RED LED OFF", bg="gray")
        red_led_button.config(text="RED LED ON")
        red_led_on = False
    else:
        red_led.on()
        red_status_label.config(text="RED LED ON", bg="red")
        red_led_button.config(text="RED LED OFF")
        red_led_on = True
        
def toggle_green_led(): 1 usage
    global green_led_on
    if green_led_on:
        green_led.off()
        green_status_label.config(text="GREEN LED OFF", bg="gray")
        green_led_button.config(text="GREEN LED ON")
        green_led_on = False
    else:
        green_led.on()
        green_status_label.config(text="GREEN LED ON", bg="green")
        green_led_button.config(text="GREEN LED OFF")
        green_led_on = True
        
def on_exit(): 1 usage
    red_led.off()
    green_led.off()
    win.destroy()

# LED 제어 버튼
red_led_button = Button(win, text="RED LED OFF", command=toggle_red_led, height=2, width=10)
red_led_button.pack(pady=10)
green_led_button = Button(win, text="GREEN LED OFF", command=toggle_green_led, height=2, width=10)
green_led_button.pack(pady=10)

# 종료 버튼
    
