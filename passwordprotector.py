# Password Protector - startkode
import random
import string

# Funksjon som skal hashe et passord
def hash_password(password):
    
    upper = random.choices(string.ascii_uppercase, k=2)
    lower = random.choices(string.ascii_lowercase, k=2)
    digits = random.choices(string.digits, k=2)
    special = random.choices("!@#$%&*-+=?", k=2)

    #plusser alt sammen
    password_list = upper + lower + digits + special
    # Bland rekkefølgen tilfeldig
    random.shuffle(password_list)
    # limer sammen alt i pasword_list til en streng
    return "".join(password_list)
    
    

# Main program starter her
password = input("Skriv inn et passord: ")

# Kall funksjonen for å hashe passordet
hashed_password = hash_password(password)

#printer ut passordet og den hashet versionen
print("Originalt passord:", password)
print("Hashet passord:", hashed_password)
