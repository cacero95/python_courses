from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.geometry("700x500")

def render_label(screen, content, config=None, anchor=None):
    render = Label(screen,content)
    if config:
        render.config(config)
    render.pack(anchor) if anchor else render.pack()

config = {
    'bg':"#2d2d2d",
    'padx':20,
    'pady':20, 
    'fg':"#ffffff",
    'font':("Consolas", 20)
}
## for expand a object into a label to the max value is neccesary el fill
# the fill indicate in what postion I want expand the content
# the side propertie indicate what position the object goint to take at the label
pack_config = {
    'side': 'top',
    'fill': 'x',
    'expand': True
}

render_label(window, {
    'text': 'Hi There'
},config, pack_config)

image = Image.open('./assets/background.png')
render = ImageTk.PhotoImage(image)

render_label(window, {
    'image':render
})

config = {
    'bg':"#2d2d2d",
    'padx':20,
    'pady':20, 
    'fg':"green",
    'font':("Consolas", 20)
}
pack_config = {
    'side': 'right'
}

render_label(window, {
    'text': 'Second label'
},config, pack_config)



config = {
    'bg':"#2d2d2d",
    'padx':20,
    'pady':20, 
    'fg':"green",
    'font':("Consolas", 20)
}
pack_config = {
    'side': 'left',
    'fill': 'x',
    'expand': True
}

render_label(window, {
    'text': 'Third label'
},config, pack_config)
config = {
    'bg':"#2d2d2d",
    'padx':20,
    'pady':20, 
    'fg':"red",
    'font':("Consolas", 20)
}
pack_config = {
    'side': 'bottom',
    'fill': 'x',
    'expand': True
}

render_label(window, {
    'text': 'Fourth label'
},config, pack_config)



window.mainloop()