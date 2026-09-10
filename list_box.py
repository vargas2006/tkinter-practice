# Listbox = A listing of selectable text items within it's own conatiner
def submit():
    food = []
    
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have oreder:")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def remove():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())




from tkinter import * 


window = Tk() 

listbox = Listbox(window,
                bg="#f0f0f0",
                font=("Arial", 12),
                width=20,
                height=5,
                selectbackground="#a6a6a6",
                selectmode=MULTIPLE,
                )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "hamburger")
listbox.insert(3, "hotdog")
listbox.insert(4, "fries")
listbox.insert(5, "soda")




entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()


addButton = Button(window, text="add", command=add)
addButton.pack()

removeButton = Button(window, text="remove", command=remove)
removeButton.pack()

window.mainloop()