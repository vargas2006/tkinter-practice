# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']


def order():
    if(x.get() == 0):
        print("You order pizza")
    elif(x.get() == 1):
        print("You order hamburger")
    elif(x.get() == 2):
        print("You order hotdog")
    else:
        print("huh?")

window = Tk()
window.title("radio btn demo")

photo = PhotoImage(file="images/picturelogo.png").subsample(2,2) # adjust the size of the image
foodImage = [photo,photo,photo]

x = IntVar()


for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                            text=food[index], #  add text to radio buttons
                            variable=x, # groups radiobuttons together if they share the same variable
                            value=index, # assign each radiobutton a different value
                            padx=25, # add padding on x-axis
                            font=("Impact", 50),
                            image = foodImage[index], # add image by index number
                            compound=LEFT, # add images and text (left-side)
                            indicatoron=0, # remove the default radio button indicator the circle dot 
                            width = 530, # sets width of radio buttons 
                            command=order, # call function order when radiobutton is clicked
                            ) 
    radiobutton.pack(anchor=W)


window.mainloop()