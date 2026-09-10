from tkinter import *
from tkinter import messagebox # import message box library

def click():
    # messagebox.showinfo(title='This is an info messagebox', message='You are a human ')
    # while(True): - fake virus
        # messagebox.showwarning(title='WARNING', message='YOU HAVE A VIRUS!!!')
    # messagebox.showerror(title="ERROR!!!", message="Something went wrong!!!")
    
    # if messagebox.askokcancel(title="ask ok cancel", message="Do u want to do the thing?"):
    #     print('You did a thing!')
    # else:
    #     print('You cancelled the thing!')

    # if messagebox.askretrycancel(title="ask retry cancel", message="Do u want to retry thes thing?"):
    #     print('You retried a thing!')
    # else:
    #     print('You cancelled a thing!')

    # if messagebox.askyesno(title="ask yes or no", message="Do u want to do the thing?"):
    #     print('You said yes!')
    # else:
    #     print('You said no!')

    # answer = messagebox.askquestion(title="ask question", message="Do u like pie?")
    # if answer == 'yes':
    #     print('You said yes!')
    # elif answer == 'no':
    #     print('why u dont like pie???')

    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?', icon='warning') # icon= warning, info or error
    if(answer == True):
        print('You like t code:')
    elif(answer == False):
        print("then why ar eu wathing on vid on coding?")
    else:
        print("You have cancel/dodged the quetion")
    

window = Tk()

button = Button(window, command=click, text='click me')
button.pack()
window.mainloop()