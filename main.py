from tkinter import *
#from gen_p import *
import random
import string 
import pyperclip 
p_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def generate_password():
    password_field.delete(0, END)
    length = 10
    password = "".join([random.choice(p_chars) for i in range (length)])
    print(password)
    pyperclip.copy(password)
    password_field.insert(0, password)
    
    
window = Tk()
window.title("Password generator")
window.config(padx=100, pady=100, bg="#E7E7E7")


greeting = Label(text="Click to button to generate a password", bg="#E7E7E7", font=("Inter", 15))
greeting.pack()


#pass_length = int(input())
button1 = Button(text="CLICK HERE", bg="#E7E7E7", font=("Inter"), command=generate_password)
button1.pack()


password_field = Entry(bg="#E7E7E7",
                       font=("Inter", 15), width=15)

password_field.pack()
#generate_password()

window.mainloop()