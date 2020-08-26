import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Menubar")

def func():
    print("func called")

#Menu : create object by creating a variable menubar, tk has a class called Menu class and pass window object in a a constructor
# menubar = tk.Menu(window)
# **************************simple menu bar****************************
# menubar.add_command(label = 'Save', command = func)
# menubar.add_command(label = 'Save As', command = func)
# menubar.add_command(label = 'Copy', command = func)
# menubar.add_command(label = 'Paste', command = func)


main_menu = tk.Menu(window) 
file_menu = tk.Menu(main_menu, tearoff = 0) 

#file menu items
file_menu.add_command(label = "New File", command = func) #dropdown items are New File, New Window and Save File, cascade items into File
file_menu.add_command(label = "New Window", command = func)
file_menu.add_separator()
file_menu.add_command(label = "Save File", command = func) 

#edit menu
edit_menu = tk.Menu(main_menu, tearoff = 0)
edit_menu.add_command(label = 'Undo', command = func)
edit_menu.add_command(label = 'Redo', command = func)

main_menu.add_cascade(label = 'File', menu = file_menu)#pass or cascade File to main menu bar
main_menu.add_cascade(label = 'Edit', menu = edit_menu)#cascade Edit to main menu bar
window.config(menu = main_menu)



window.mainloop()
