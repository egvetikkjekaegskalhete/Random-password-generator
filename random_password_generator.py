#Random Password Generator - www.101computing.net/random-password-generator/
import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1 = chr(random.randint(65, 90))  # Store bokstaver
uppercaseLetter2 = chr(random.randint(65, 90))

lowercaseLetter1 = chr(random.randint(97, 122))  # Små bokstaver
lowercaseLetter2 = chr(random.randint(97, 122))

digit1 = chr(random.randint(48, 57))  # Sifre
digit2 = chr(random.randint(48, 57))

special_chars = "!#$@?-*+="
special1 = random.choice(special_chars)  # Spesialtegn
special2 = random.choice(special_chars)



#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + special1 + special2

password = shuffle(password)

#Ouput
print(password)
