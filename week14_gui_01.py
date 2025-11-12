import tkinter as tk

def get_input_value():
    # print(en_input.get())
    lbl_display.config(text=en_input.get())
    # click 누르면 en_input에 입력된 텍스트가 lbl_display에 적용
    
win = tk.Tk() # 윈도우 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click', width=15, command=get_input_value)
lbl_display = tk.Label(win, text = 'Display', width=30)

# layout (grid : 행열)
lbl_display.grid(row=0, column=0, columnspan=2, sticky='EW')
en_input.grid(row=1, column=0, sticky='EW') # NESW = 동서남북
btn_click.grid(row=2, column=1, sticky='EW') # grid는 sticky 필요

win.mainloop()