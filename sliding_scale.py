from tkinter import *

def submit():
    print("The current value is: " + str(scale.get()) + "°C")

window = Tk()

scale = Scale(window,
            from_=0,
            to=100,
            length=600,
            orient=VERTICAL, # orientation of scale
            font=('consolas', 20),
            tickinterval=10, # adds numeric indicators for value
            showvalue=0, # hide current value
            troughcolor='gray',
            fg='red',
            bg='black',
            resolution=0.5 # set increments of the scale
            
            )

scale.set(50) # set initial value
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()