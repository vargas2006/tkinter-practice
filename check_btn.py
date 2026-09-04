from tkinter import *



window = Tk()

x = IntVar() # to keep track of the check button u can change the type of data depends on the return
photo = PhotoImage(file="images/picturelogo.png")
def display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("You disagree")

check_button = Checkbutton(window,
                            text="I agree to something",
                            variable=x,
                            onvalue=1, # u can change it to boolean but u have to change the IntVar() to BooleanVar() to make it work properly
                            offvalue=0, # u can change it to boolean but u have to change the IntVar() to BooleanVar() to make it work properly
                            command=display,
                            font=('Arial', 20),
                            bg='blue',
                            fg='white',
                            activeforeground='green',
                            activebackground='black',
                            padx=25,
                            pady=10,
                            image=photo,
                            compound=LEFT,
                            
                            ) 
check_button.pack()

window.mainloop()