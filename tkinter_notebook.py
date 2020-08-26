"""
#notebook
#page 1           #page 2
#widgets          #widgets
1) nb.pack(expand = True, fill = 'both')

"""
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("TAB CONTROL")
nb = ttk.Notebook(window)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text = "PAGE ONE")
nb.add(page2, text = "PAGE TWO")

#nb.grid(row =0, column = 0)
#to expand both horizontally and vertically
nb.pack(expand = True, fill = 'both')

label1 = ttk.Label(page1, text = 'This is label 1')
label1.grid(row = 0 , column = 0)

entry1 = ttk.Entry(page1, width = 26)
entry1.grid(row = 0, column = 1)

label2 = ttk.Label(page2, text = 'This is label 2')
label2.grid(row = 0 , column = 0)

entry2 = ttk.Entry(page2, width = 26)
entry2.grid(row = 0, column = 1)

window.mainloop()