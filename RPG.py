from tkinter import *
import string
import random


def RPG():
   s1 = string.ascii_lowercase
   s2 = string.ascii_uppercase
   s3 = string.punctuation
   s4 = string.digits

   dig = int(e1.get())
   
   password = []
   password.append(random.choice(s2))
   password.append(random.choice(s3))
   password.append(random.choice(s4))
   password.extend(list(s1))
   password.extend(list(s2))
   password.extend(list(s3))
   password.extend(list(s4))
   random.shuffle(password)
   s = "".join(password[0:dig])
   result_label.config(text=f'YOUR PASSWORD IS {s}')

master = Tk()
master.title("Random Password Generator")
master.geometry("400x150")

Label(master, text='Enter Length Of Password').grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

calculate_button = Button(master, text="Generate", command=RPG)
calculate_button.grid(row=3, columnspan=2)#3 2

result_label = Label(master, text='   ',)
result_label.grid(row=5, columnspan=4)#5 4

mainloop()

