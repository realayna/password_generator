from tkinter import *

import random
import string 
import pyperclip 

p_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def generate_password():
    length = 10
    password = "".join([random.choice(p_chars) for i in range (length)])
    print(password)
    pyperclip.copy(password)
    
    