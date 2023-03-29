from tkinter import *
from gen_p import *

import random
import string 

window = Tk()
window.title("Password generator")
window.config(padx=100, pady=100, bg="#E7E7E7")
greeting = Label(text="Click to button to generate a password", bg="#E7E7E7", font=("Inter", 15))
greeting.pack()
pass_length = int(input())
button1 = Button(text="CLICK HERE", bg="#E7E7E7", font=("Inter") )
button1.pack()
generate_password()

window.mainloop()