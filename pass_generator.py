import random
import string

#Password Generator Program
#Coded by David Cui
#Completed: 6/23/2023

#Password Generator
"""
    generate a random password of 8 characters. 
    Each time the program is run, a new password will be 
    generated randomly. The passwords generated will be 
    8 characters long and will have to include the following characters in any order:
        2 uppercase letters from A to Z,
        2 lowercase letters from a to z,
        2 digits from 0 to 9,
        2 punctuation signs such as !, ?, “, # etc.
"""
#Data Sets
letters = ["a", "b", "c", "d", "e",
          "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o",
          "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

punct = string.punctuation

#Password
password = ""

def uppercase1():
    return random.choice(letters).upper()

def uppercase2():
    return random.choice(letters).upper()

def lowercase1():
    return random.choice(letters)

def lowercase2():
    return random.choice(letters)

def digit1():
    return random.choice(numbers)

def digit2():
    return random.choice(numbers)

def punct1():
    return random.choice(punct)

def punct2():
    return random.choice(punct)

def final_password():
    password = uppercase1() + uppercase2() + lowercase1() + lowercase2() + str(digit1()) + str(digit2()) + punct1() + punct2()
    password = list(password)
    random.shuffle(password)
    password = ''.join(password) #This operation joins the different characters together from the list of characters
    print(password)
    
generated_passsword = final_password()
print(generated_passsword)
