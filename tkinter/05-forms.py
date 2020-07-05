from tkinter import *

window = Tk()

window.geometry("700x400")
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