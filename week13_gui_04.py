import tkinter as tk

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
led = False

def led_on(): 1 usage
    #print("LED 켜짐")
    if led:
        lbl_display.config(text="LED 켜짐")
        GPIO.output(LED_PIN, GPIO.LOW)
        led = False
    else:
        lbl_display.config(text="LED 꺼짐")
        GPIO.output(LED_PIN, 1)
        led = True
    
win = tk.Tk() # 윈도우 객체 생성
win.title("GUI")
win.geomerty("400x200")

btn_on_off = tk.Button(win, text="LED ON", command=toggle_led, height=2, width=10)
btn_on_off = tk.Button(win, text="LED EXIT", command=on_exit, height=2, width=10)
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성

lbl_display.pack()
btn_click.pack(fill='x')

win.mainloop()


