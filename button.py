from tkinter import *

#  button = you click it, then i does stuffs
count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='images/picturelogo.png') # add image to the window

button = Button(window, # create button in the window
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="green",
                bg="black",
                activeforeground="green", # change color when clicked
                activebackground="black", # change background color when clicked
                state=ACTIVE, # DISABLE = cant click, ENABLE = can click, ACTIVE = click
                image=photo, # add photo
                compound="top" # adjust the position of the image and text
                
                )
button.pack()

window.mainloop()
