from tkinter import *

window = Tk()
window.geometry("700x700")

window.config(bg="#2d2d2d", bd=50)

def getData():
    # the set overwrite the data into the variable
    result.set(data.get())
    if len(result.get()) >= 1:
        out.config(
            bg="red",
            fg="#000000"
        )

# for collect data is neccesary the use of StringVar
data = StringVar()
result = StringVar()

Label(window, text="Type your text").pack(anchor="nw")
Entry(window, textvariable=data).pack(anchor="nw")

Label(window, text="Your data is").pack(anchor="nw")
out = Label(window, textvariable=result)

out.pack(anchor="nw")

Button(window, text="show data", command=getData).pack()

window.mainloop()