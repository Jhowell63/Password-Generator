import random
import string


def generate_password(pwd_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    

    while not meet_criteria or len(pwd) < pwd_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        if len(pwd) > pwd_length:
            pwd = pwd[:pwd_length]

    return pwd        

min_length = int(input("Enter the minimim length: "))
max_length = int(input("Enter the max length: "))
if max_length > 20:
    password_length = random.randint(min_length, 20)
else:
    password_length = random.randint(min_length, max_length)

has_number = input("Do you want to have numbers (y/n): ").lower() == "y"
has_special = input("Do you want to have special characters (y/n): " ).lower() == "y"


pwd = generate_password(password_length, has_number, has_special)

print("The generated password is : ", pwd)
print(password_length) 