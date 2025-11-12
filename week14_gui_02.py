import tkinter as tk
from gpiozero import LED

def get_input_value():
    num = en_input.get()
    if num == "1":
        red_led.on()
        lbl_display.config(text='LED_ON')
    elif num == "0":
        red_led.off()
        lbl_display.config(text='LED_OFF')
    else:
        lbl_display.config(text='0 또는 1을 입력하세요.')
    # print(en_input.get())
    lbl_display.config(text=en_input.get())
    
    
red_led = LED(16)

win = tk.Tk() # 윈도우 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click', width=15, command=get_input_value)
lbl_display = tk.Label(win, text = 'Display', width=30)

lbl_display.grid(row=0, column=0, columnspan=2, sticky='EW')
en_input.grid(row=1, column=0, sticky='EW') # NESW = 동서남북
btn_click.grid(row=2, column=1, sticky='EW') # grid는 sticky 필요

win.mainloop()