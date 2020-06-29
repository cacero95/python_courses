from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Frames on Tkinter")
window.geometry("700x700")

def render_label(screen, content, config=None, anchor=None):
    render = Label(screen,content)
    if config:
        render.config(config)
    render.pack(anchor) if anchor else render.pack()

top_frame = Frame(window, height=250)
top_frame.pack(anchor="n", fill="x", expand=True)

bottom_frame = Frame(window, height=250)
bottom_frame.pack(anchor="s", fill="x", expand=True)

frame = Frame(top_frame, width=250, height=250)
# bd is the border in css
# relief is the type of borders: border types 'flat, groove, raised, ridge, solid, or sunken'

frame.config(
    bg="red",
    bd=12,
    relief="solid"
)

frame.pack(side="left")
frame.pack_propagate(False)
render_label(frame, {"text":"First frame"},{"bg":"#2d2d2d", "fg":"#ffffff"},{"fill":'y', "anchor":"center", 'expand':True})


frame = Frame(top_frame, width=250, height=250)
frame.config(
    bg="blue",
    bd=12,
    relief="solid"
)

frame.pack(side="right")
frame.pack_propagate(False)
# render a image into a frame
image = Image.open('./assets/background.png')
render = ImageTk.PhotoImage(image)

render_label(frame,{"image":render},{"anchor":"e"})

frame = Frame(bottom_frame, width=250, height=250)
frame.config(
    bg="orange",
    bd=12,
    relief="solid"
)

frame.pack(side="right")

frame = Frame(bottom_frame, width=250, height=250)
frame.config(
    bg="#cccccc",
    bd=12,
    relief="solid"
)

frame.pack(side="left")

window.mainloop()