from tkinter import *
master = Tk()
w=Canvas(master, width=400, height=400)
w.pack()

for j in range(4):
    for i in range(4):
        ox= 40 * i
        oy = 40 * j
        w.create_rectangle(0 + ox, 0 + oy, 20 + ox, 20 + oy, fill='#000000')
        w.create_rectangle(20 + ox, 20 + oy, 40 + ox, 40 + oy, fill='#000000')


mainloop()
