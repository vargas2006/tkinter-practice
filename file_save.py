from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(
                                    initialdir="C:/tkinter",
                                    defaultextension='.txt',
                                    filetypes=[("Text Files", "*.txt"),("HTML Files", "*.html"), ("All Files", "*.*")]
                                    )
    if file is None: # para hindi mag error pag wala kang input
        return
    filetext = str(text.get(1.0, END)) 
    # filetext = input("Enter some text I guess:")
    file.write(filetext)
    file.close()
    

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()


window.mainloop()