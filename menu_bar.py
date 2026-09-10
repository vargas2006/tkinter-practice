from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You cut text!")

def copy():
    print("You copied text!")

def paste():
    print("You pasted text!")

def quit():
    window.destroy()

window = Tk()

openImage = PhotoImage(file="images/file.png")
saveImage = PhotoImage(file="images/save.png")
quitImage = PhotoImage(file="images/exit.png")

menubar = Menu(window)
window.config(menu=menubar)


fileMenu = Menu(menubar, tearoff=0, font=("MV boli", 15))
menubar.add_cascade(label="File", menu=fileMenu, image=openImage)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=quitImage, compound="left")

editMenu = Menu(menubar, tearoff=0, font=("MV boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()