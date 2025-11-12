import tkinter as tk

def led_on():
    #print("LED 켜짐")
    lbl_display.config(text="LED 켜짐")
    
def led_on():
    lbl_display.config(text="LED 꺼짐")
    
win = tk.Tk() # 윈도우 객체 생성
win.title("GUI")
win.geomerty("400x200")

btn_on = tk.Button(win, text="LED ON", command=led_on) # 버튼 객체 생성
btn_off = tk.Button(win, text="LED OFF", command=led_off)
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성

lbl_display.pack()
btn_click.pack(fill='x')

win.mainloop()
