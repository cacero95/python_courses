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

window.mainloop()