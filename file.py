from tkinter import *
from tkinter import filedialog

window = Tk()

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\tkinter",
                                        title="Open file okay?",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    file = open(filepath, 'r')
    print(file.read())
    file.close()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()