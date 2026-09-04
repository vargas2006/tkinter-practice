from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


window = Tk() # make a window
window.geometry("420x420") # adjust the size of the window
window.title("tkinter practice") # change title of the window

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon) # change the icon of the window
window.config(background="black") # change the background color of the window



window.mainloop() # display window / place window on computer screen, listen for events