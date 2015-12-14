from tkinter import *
master = Tk()
w=Canvas(master, width=400, height=400)
w.pack()

for i in range(1, 400, 10):
    x = i
    y = 400 - x
    w.create_line(x, 0, 0, y, fill='#000000', width=1)

mainloop()
