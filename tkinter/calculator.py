from tkinter import *
from tkinter import messagebox as mess
import os.path as PATH

class Window:

    def __init__(self, title, is_resize, icon, size, config=None):
        
        self.title = title
        self.is_resize = is_resize
        self.size = size
        if not PATH.isfile(icon):
            icon = f"./tkinter/{icon}"
        self.icon = icon
        self.window = Tk()

        # Resize the window
        self.window.geometry(self.size)

        # Rename the window
        self.window.title(self.title) 

        # Block the size of the window
        # firs position catch the events on x and the second is the y
        self.window.resizable(0,0) if not self.is_resize else self.window.resizable(1,1)
    
        # window icon have take a ico image for render
        self.window.iconbitmap(self.icon)

        # config the main window
        if config:
            self.window.config(config)

    def showWindow(self):
        self.window.mainloop()
    def getWindow(self):
        return self.window
"""
    1. object to render
    2. content into the rendered object
    3. config like styles ! optional
    4. position on the pack ! optional
    5. the pack propate ! optional
"""
def render_pack(render_object, config=None, anchor=None, propagate=True):
    if config:
        render_object.config(config)
    render_object.pack(anchor) if anchor else render_object.pack()
    render_object.pack_propagate(propagate)
    return render_object

"""
    1. object to render
    2. content into the rendered object
    3. config like styles ! optional
    4. position on the pack or grid ! optional
"""
def render_grid(render_object, config=None, anchor=None):
    if config:
        render_object.config(config)
    render_object.grid(anchor) if anchor else render_object.grid()
    return render_object

def showMessage(value):
    result.set(value)
    mess.showinfo('Result',f'result {result.get()}')
    number1.set('')
    number2.set('')

def comprobate_number(number_input):
    try:
        return float(number_input)
    except:
        mess.showerror("Error Formatting", "Let me see, do a calculator with something different to numbers")

window = Window('first', False,'assets/Pikachu-portada-1.ico','400x400',{'bg':'#2d2d2d'})
actual_window = window.getWindow()

number1 = StringVar()
number2 = StringVar()
result = StringVar()

mark = render_pack(
    Frame(actual_window, width=220, height=250),
    {
        "bd":5,
        "padx":5,
        "pady":5
    },
    {
        "side":"top",
        "anchor":"center"
    },
    False
)

render_pack(
    Label(mark, text="First Number:")
)

render_pack(
    Entry(mark, textvariable=number1, justify="center")
)

render_pack(
    Label(mark, text="Second Number:")
)

render_pack(
    Entry(mark, textvariable=number2, justify="center")
)

render_pack(
    Label(mark, text="")
)

render_pack(
    Button(mark, text="Sumar", command=lambda: showMessage( comprobate_number(number1.get()) + comprobate_number(number2.get()) )),
    None,
    {'side':'left','fill':'x','expand':True}
)


render_pack(
    Button(mark, text="Restar", command=lambda: showMessage( comprobate_number(number1.get()) - comprobate_number(number2.get()) )),
    None,
    {'side':'left','fill':'x','expand':True}
)
render_pack(
    Button(mark, text="Multipicar", command=lambda: showMessage( comprobate_number(number1.get()) * comprobate_number(number2.get()) )),
    None,
    {'side':'left','fill':'x','expand':True}
)
render_pack(
    Button(mark, text="Dividir", command=lambda: showMessage( comprobate_number(number1.get()) / comprobate_number(number2.get()) )),
    None,
    {'side':'left','fill':'x', 'expand':True}
)


window.showWindow()
