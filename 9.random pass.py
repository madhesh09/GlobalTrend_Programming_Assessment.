import random
import string

def generate_random_password(length):
    if length < 5:  
        raise ValueError("Password length is less than 5")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_char)
    ]
    all_characters = uppercase + lowercase + digits + special_char
    password += random.choices(all_characters, k=length-4)
    
    random.shuffle(password)
    
    return ''.join(password)
password = generate_random_password(7)
print("Generated Password:", password)

