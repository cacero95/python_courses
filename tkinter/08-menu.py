from tkinter import *

window = Tk()

window.geometry("500x500")
main_menu = Menu(window)
window.config(menu=main_menu)

# the file will be a sub menu of the main_menu and the tearoff=0 quit the initial separator
file = Menu(main_menu, tearoff=0)
file.add_command(label='new file')
file.add_command(label='new window')
# the separator create a separator between two labels
file.add_separator()
file.add_command(label='open file')
file.add_command(label='open folder')
file.add_separator()
# window.quit close the window
file.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Selection")

window.mainloop()