import tkinter as tk

led = False

def led_on(): 1 usage
    #print("LED 켜짐")
    if led:
        lbl_display.config(text="LED 켜짐")
        led = False
    else:
        lbl_display.config(text="LED 꺼짐")
        led = True
    
win = tk.Tk() # 윈도우 객체 생성
win.title("GUI")
win.geomerty("400x200")

btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on) # 버튼 객체 생성
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성

lbl_display.pack()
btn_click.pack(fill='x')

win.mainloop()

