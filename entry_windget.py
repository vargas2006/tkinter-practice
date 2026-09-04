from tkinter import *
# entry widget = textbox that accepts a single line of user input

def submit():
    username= entry.get()
    print("Hello "+username) # get the input
    # entry.config(state=DISABLED)  lock the entry

def delete():
    entry.delete(0, END) # delete everthing

def backspace():
    entry.delete(len(entry.get())-1, END) # delete one by one backspace

window = Tk()

entry = Entry(window,
            font=('Arial', 16),
            fg="green",
            bg="black",
            show="*", # hide the input
            )

entry.insert(0, 'Enter username') # default text on the entry box
entry.pack(side=LEFT)

submit_button = Button(window, 
                    text="submit",
                    command=submit, 
                    )
submit_button.pack(side=LEFT)

delete_button = Button(window, 
                    text="delete",
                    command=delete, 
                    )
delete_button.pack(side=LEFT)

backspace_button = Button(window, 
                    text="backspace",
                    command=backspace, 
                    )
backspace_button.pack(side=LEFT)



window.mainloop()