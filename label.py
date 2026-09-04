from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

icon = PhotoImage(file='picturelogo.png')

label = Label(window,   # design the label / add label
            text="Hello World", 
            font=('Arial',18,'bold'), 
            fg='green', # font color
            bg='black', # background color
            relief=FLAT, # border style
            bd=2, # border width
            padx=20, # add padding
            pady=20, # add padding 
            image=icon, # add image
            compound='bottom' # adjust the position of the image
            )
label.pack() # = by default it display in the center, top to bottom
#label.place(x=0, y=0) # = it will display specificly based on the coordinate

window.mainloop()
