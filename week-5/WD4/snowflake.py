from tkinter import *
master = Tk()
w=Canvas(master, width=400, height=400)
w.pack()


w.create_line(200, 0, 200, 400, fill='#000000', width=1)
w.create_line(0, 300, 400, 100, fill='#000000', width=1)
w.create_line(0, 100, 400, 300, fill='#000000', width=1)


#
# for i in range(1, 400, 10):
#     x = i
#     y = 400 - x
#     w.create_line(x, 0, 0, y, fill='#000000', width=1)

mainloop()
