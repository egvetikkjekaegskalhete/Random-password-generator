# Password Protector - startkode
import hashlib

# Funksjon som skal hashe et passord
def hash_password(password):
    # fullfør koden her
    return ??? #fullfør koden her

# Main program starter her
password = input("Skriv inn et passord: ")

# Kall funksjonen for å hashe passordet
hashed_password = hash_password(password)

# Output
print("Originalt passord:", password)
print("Hashet passord:", hashed_password)
