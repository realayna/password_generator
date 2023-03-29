import random
import string 



p_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def generate_password():
    length = pass_length
    password = "".join([random.choice(p_chars) for i in range (length)])
    print(password)