# frame = a rectanglar container to group and hold widgets
from tkinter import *

window = Tk()
frame = Frame(window, bg="grey", bd=5, relief=RAISED)
frame.pack()

button = Button(frame, text ="W", font=("Consolas", 30), width=3).pack(side=TOP)
button = Button(frame, text ="A", font=("Consolas", 30), width=3).pack(side=LEFT)
button = Button(frame, text ="S", font=("Consolas", 30), width=3).pack(side=LEFT)
button = Button(frame, text ="D", font=("Consolas", 30), width=3).pack(side=LEFT)








window.mainloop()
