from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(
    bg="#2d2d2d"
)

### config properties ###
###
# 
# bg = background
# fg = color css
# padx = padding x
# pady = padding y
# font = typing the text like font-size and font-family
# anchor = change the position of an object n, ne, e, se, s, sw, w, nw, or center
# cursor = change the cursor form 
# 
# ###

def setText(config, content, anchor=None):
    txt = Label(window, text=content)
    txt.config(config)
    #if is neccesary change the position of a object at the ui
    #use de anchor with next properties n, ne, e, se, s, sw, w, nw, or center into the pack()
    txt.pack(anchor=anchor) if anchor else txt.pack()
config = {
    'bg':"#2d2d2d",
    'padx':20,
    'pady':20, 
    'fg':"#ffffff",
    'font':("Consolas", 20)
}
setText(config,'Hi there', 'center')

config = {
    'justify':"right",
    'width':200,
    'height':10,
    'anchor': 'center',
    'cursor':'spider'
}
setText(config,'My name is Carlos Acero')

window.mainloop()