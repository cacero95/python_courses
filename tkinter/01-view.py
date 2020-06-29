from tkinter import * 
import os.path as PATH

class Window:

    def __init__(self, title, is_resize, icon, size):

        self.title = title
        self.is_resize = is_resize
        icon = PATH.abspath(icon)
        if not PATH.isfile(icon):
            icon = f"./tkinter/{icon}"
        self.icon = icon
        self.size = size
        # Create a window
        self.window = Tk()

    def prepare_window(self):

        # Resize the window
        self.window.geometry(self.size)

        # Rename the window
        self.window.title(self.title) 

        # Block the size of the window
        # firs position catch the events on x and the second is the y
        self.window.resizable(0,0) if self.is_resize else self.window.resizable(1,1)
    
        # window icon have take a ico image for render
        self.window.iconbitmap(self.icon)

    def addText(self, word):
        # for show label at the window
        txt = Label(self.window, text=word)
        txt.pack()

    def showWindow(self):

        # the loop show the window all the time
        self.window.mainloop()

window = Window('first', True,'assets/Pikachu-portada-1.ico','770x470')
window.prepare_window()
window.addText('Hello world')
window.addText('Hello world')
window.addText('Hello world')
window.showWindow()