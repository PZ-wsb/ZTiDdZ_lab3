import string
import random

def tworzenie_hasla():
    Znaki = list(string.ascii_letters + string.digits + string.punctuation)
    litery_male = list(string.ascii_lowercase)
    litery_duze = list(string.ascii_uppercase)
    znaki = list(string.punctuation)
    cyfry = list(string.digits)

    length = random.randint(8,15)
    random.shuffle(Znaki)

    password = []
    password.append(random.choice(litery_male))
    password.append(random.choice(litery_duze))
    password.append(random.choice(znaki))
    password.append(random.choice(cyfry))

    for i in range(length-4):
	    password.append(random.choice(Znaki))

    random.shuffle(password)
    print("".join(password))

tworzenie_hasla()