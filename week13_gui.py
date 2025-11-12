import tkinter as tk

win = tk.Tk()
win.title("GUI")
win.geomerty("400x200")
win.resizeable(width False, height False)

btn_test = tk.Button(win, text="IoT GUI 실습 중...")
btn_test.pack()

win.mainloop()