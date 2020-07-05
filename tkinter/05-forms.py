from tkinter import *

window = Tk()

window.geometry("700x800")
window.title("First form with tkinter")

def render_label(screen, content, config=None, anchor=None):
    render = Label(screen,content)
    if config:
        render.config(config)
    render.pack(anchor) if anchor else render.pack()

top_frame = Frame(window)
top_frame.config({
    "pady":20,
    "bg":"#ffffff"
})
top_frame.pack(anchor="n", fill="x", expand=True)
render_label(top_frame,
    {
        "text":"Forms with tkinter"
    },
    {
        "fg":"#ffffff",
        "bg":"#2d2d2d",
        "font":("consolas", 18),
        "height":2,
        "pady":20,
        "padx":10
    }
)

center_frame = Frame(window, width=100, height=20)
center_frame.config({
    "pady":10,
    "padx":20,
    "bg":"#ffffff"
})
center_frame.pack(anchor="n", expand=True)

center_first = Frame(center_frame, width=80)
center_first.pack(side="top", anchor="nw")


render_label(center_first,
    {
        "text":"Name"
    },
    {
        "font":("consolas", 10),
        "height":1,
        "width":20
    },
    {
        "anchor":"ne",
        "side":"left"
    }
)



# center_frame.pack_propagate(False)
# for define a for is neccesary use the entry object
text_field = Entry(center_first)
text_field.pack(anchor="nw", side="right")

center_second = Frame(center_frame, width=80)
center_second.pack(side="top", anchor="nw")

render_label(center_second,
    {
        "text":"LastName"
    },
    {
        "font":("consolas", 10),
        "height":1,
        "width":20
    },
    {
        "anchor":"e",
        "side":"left"
    }
)

# center_frame.pack_propagate(False)
# for define a for is neccesary use the entry object
text_field = Entry(center_second)
text_field.pack(anchor="w", side="right")

center_third = Frame(center_frame, width=80)
center_third.pack(side="top", anchor="nw")

render_label(center_third,
    {
        "text":"Description"
    },
    {
        "font":("consolas", 10),
        "height":1,
        "width":20
    },
    {
        "anchor":"e",
        "side":"left"
    }
)
# TextArea in tkinter
textArea = Text(center_third)
textArea.config(width=30, height=5)
textArea.pack(side="right")

center_thirdHalf = Frame(center_frame, width=80)
center_thirdHalf.pack(side="top", anchor="nw")


web = IntVar()
mobile = IntVar()

def onClick():
    if web.get():
        Label(center_thirdHalf, text=f"Desarrollo web").pack(anchor="w")
    if mobile.get():
        Label(center_thirdHalf, text=f"Desarrollo mobile").pack(anchor="w")

Checkbutton(center_thirdHalf, text="web Develop", variable=web, onvalue=1, offvalue=0, command=onClick).pack(anchor="w")
Checkbutton(center_thirdHalf, text="mobile Develop", variable=mobile, onvalue=1, offvalue=0, command=onClick).pack(anchor="w")

def markRadio():
    if options.get():
        radio_label.config(text=options.get())

options = StringVar()
# for desmark the radio options have to take a None value by default
options.set(None)
# Radio button
Radiobutton(center_thirdHalf, text="Male", value="male", command=markRadio, variable=options).pack(anchor="w")
Radiobutton(center_thirdHalf, text="Female", value="female", command=markRadio, variable=options).pack(anchor="w")
radio_label = Label(center_thirdHalf, text="")
radio_label.pack()

# options menu
menu_option = StringVar()
menu_option.set('Option 1')
OptionMenu(window, menu_option, "Option 1", "Option 2").pack(side="top", anchor="nw")


center_fourth = Frame(center_frame, width="80")
center_fourth.config(
    bg="#ffffff",
    pady=20
)
center_fourth.pack(side="top")

# Buttons in tkinter
button = Button(center_fourth, text="Send")
button.config(pady=20, padx=20)
button.pack()

window.mainloop()