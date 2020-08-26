
import tkinter as tk

from tkinter import ttk

window = tk.Tk() 

window.title("GUI")

#creating labels

#first method
#ttk.Label(window, text = "Enter your name:").pack()

#second method: label.grid(column = 0, row = 0) #at the first position
#ttk.Label(window, text = "Enter your name:").grid(column = 0, row = 0)

#third way : create variable ansd call instance
name_label = ttk.Label(window, text = "Enter your name:")
name_label.grid(row=0, column=0, sticky = tk.W)

#STICKY - will stick the allignment to the left and tk.W , here W is west direction
email_label = ttk.Label(window, text = "Enter your email:")
email_label.grid(row = 1, column = 0, sticky = tk.W)

age_label = ttk.Label(window, text = "Enter your age:")
age_label.grid(row = 2, column = 0, sticky = tk.W)

gender_label = ttk.Label(window, text = "Enter your gender:")
gender_label.grid(row = 3, column = 0, sticky = tk.W)


#create entry box , but we have to create a variable where the user information will be stored
name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width = 16, textvariable = name_var)
name_entrybox.grid(row = 0, column = 1)
name_entrybox.focus()


email_var = tk.StringVar()
email_entrybox = ttk.Entry(window, width = 16, textvariable = email_var)
email_entrybox.grid(row = 1, column = 1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(window, width = 16, textvariable = age_var)
age_entrybox.grid(row = 2, column = 1)


#create combobox - we can create dropdown so that user can select from multiple options
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window, width = 14, textvariable = gender_var, state = 'readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row = 3, column = 1)

#create radio button : Student, Teacher #StringVar should be same for both teahcer snd student, so that any one can be cjhoose but not both
usertype = tk.StringVar()
radiobutton1 = ttk.Radiobutton(window, text = 'Student', value = 'Student', variable = usertype)
radiobutton1.grid(row = 4, column = 0)

radiobutton2 = ttk.Radiobutton(window, text = 'Teacher', value = 'Teacher', variable = usertype)
radiobutton2.grid(row = 4, column = 1)

#check button
checkbutton_var = tk.IntVar() # if check valur id drlcted then 1 otherwise 0
check_button = ttk.Checkbutton(window, text = "Check if you want to subscribe our Newsletter", variable = checkbutton_var)
check_button.grid(row = 5, columnspan = 3)

#get() allows us to get the value of name, age, email, usertypr, gender type, checkbox status

def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f"{username} is {userage} is years old and account is {user_email}")

    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbutton_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'
    
    print(user_gender, user_type, subscribed)
    
    with open('file.txt', 'a') as f:
        f.write(f"{username}, {userage}, {user_email}, {user_gender}, {user_type}, {subscribed}\n")

    #to make entryboxes empty after every input submitted
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    #to configure color, either use basic color or color picker from google
    name_label.configure(foreground = '#b388ff')


submit_button = ttk.Button(window, text = 'Submit', command = action)
submit_button.grid(row = 6, column = 0)



window.mainloop()
