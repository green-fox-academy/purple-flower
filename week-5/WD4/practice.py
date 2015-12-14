from tkinter import *
master = Tk()
w=Canvas(master, width=400, height=400)
w.pack()
w.create_rectangle(0, 0, 160, 160, fill='#ffffff')

w.create_rectangle(0, 0, 20, 20, fill='#000000')
w.create_rectangle(40, 0, 60, 20, fill='#000000')

w.create_rectangle(20, 20, 40, 40, fill='#000000')
w.create_rectangle(60, 20, 80, 40, fill='#000000')

w.create_rectangle(0, 40, 20, 60, fill='#000000')



mainloop()
