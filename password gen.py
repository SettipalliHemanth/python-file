import random
import string
def genarate_password(min_length,number=True,special_characters=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    characters = s1
    if number:
        characters +=s2
    if special_characters:
        characters += s3

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password)< min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in s2:
            has_number = True 
        elif new_char in s3:
            has_special = True
        meets_criteria = True

        if number:
            meets_criteria += has_number 
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return password
min_length  = int(input("Enter password length: "))
has_number = input("if you want numbers (y/n)").lower() == 'y'
password = genarate_password(min_length,has_number)
print('your password : ',password)


             

    

