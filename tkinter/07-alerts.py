from tkinter import *
from tkinter import messagebox as Messabox

window = Tk()

def showAlert():
    # types of alerts
    Messabox.showinfo("alert", 'Hi there')
    Messabox.showwarning("alert", 'Hi there')
    Messabox.showerror("alert", 'Hi there')

Button(window, text="Show Alert!!!", command=showAlert).pack()

def exit(name):
    # types of questions
    result = Messabox.askquestion("Exit", 'Are you go')
    if result != "no":
        Messabox.showinfo('bye', f"Bye {name}")
        window.destroy()

# Button(window, text="Questions!!!", command=exit).pack()
# if is neccesary set a params into the method with a eventlistenner is neccesary the lambda function
Button(window, text="Questions!!!", command=lambda: exit('Andres')).pack()

window.mainloop()