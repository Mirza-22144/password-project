#password gen


import secrets
import string

# Defining the password generator
def password_generation(pwd_min_length=20, numbers=True, special_characters=True): 
    letters = string.ascii_letters
    digits = string.digits
    special_ch = string.punctuation

    pwd_characters = letters 
    if numbers:
        pwd_characters += digits
    if special_characters:
        pwd_characters += special_ch

    meets_criteria = False

    while not meets_criteria or len(pwd) < pwd_min_length:
        pwd = ''
        has_number = False
        has_special = False

        for _ in range(pwd_min_length):
            add_new_char = secrets.choice(pwd_characters)
            pwd += add_new_char

            if add_new_char in digits:
                has_number = True
            if add_new_char in special_ch:
                has_special = True

        meets_criteria = True
        if numbers and not has_number:
            meets_criteria = False
        if special_characters and not has_special:
            meets_criteria = False

    return pwd



# Get user input, ensuring strings as a alpha
has_number = input("Do you want numbers in your password? (Y/N): ").strip().upper() == 'Y'
has_special = input("Do you want special characters in your password? (Y/N): ").strip().upper() == 'Y'

# Generate and print password
pwd = password_generation(20, has_number, has_special)
print('Your new generated password is:',[ pwd ])

 
        
    
    





    