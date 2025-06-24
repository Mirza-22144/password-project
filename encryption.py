# """this password encryption app uses a ceasar cypher encryption. Usallay only used with letters i have implemnete it on numbers and special charcters."""



#password gen



import random
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

 
        
    
    




#________________________________________________________





#password encryption 

def pwd_encrypt_cypher(generated_pwd):
    # Character sets
    pwd_lett = string.ascii_letters
    pwd_digits = string.digits
    pwd_special_ch = string.punctuation

    # Combine all valid charactersy
    pwd_library = pwd_lett + pwd_digits + pwd_special_ch

    # Choose a random Caesar cipher shift (1–25)
    shift = random.randint(1, 25)

    encrypted = ""

    for char in generated_pwd:
        if char in pwd_lett:
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char in pwd_digits:
            encrypted += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        elif char in pwd_special_ch:
            index = pwd_special_ch.index(char)
            encrypted += pwd_special_ch[(index + shift) % len(pwd_special_ch)]
        else:
            encrypted += char  

    return encrypted


# Ask user if they want encryption
encrypt_choice = input("Do you wish to encrypt the password? (Y/N): ").strip().upper()

if encrypt_choice == 'Y':
    encrypted_pwd = pwd_encrypt_cypher(pwd)  
    print("Your encrypted password is:", encrypted_pwd)
    
else:
    print("OK, your password was not encrypted.") 