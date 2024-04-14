import random
import string
import os

def generatepassword(length, charactertypes):
    characters = ''
    for chartype, symbols in charactertypes.items():
        if chartype:
            characters += symbols

    if not characters:
        raise ValueError("At least one character type should be selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def calculatestrength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

def main():
    print("Greetings! I'm your trusty Password Generator.")

    charactertypes = {
        'letters': string.ascii_lowercase,
        'uppercaseletters': string.ascii_uppercase,
        'numbers': string.digits,
        'symbols': '!@#$%^&*()-=[]{}|;:,.<>?'
    }

    try:
        length = int(input("How long would you like your password to be? (minimum 6): "))
        if length < 6:
            raise ValueError("Password length should be at least 6 characters.")
    except ValueError as ve:
        print("Whoops! That's not a valid length:", ve)
        return

    useletters = input("Would you like to include lowercase letters? (yes/no): ").lower() == 'yes'
    useuppercaseletters = input("Would you like to include uppercase letters? (yes/no): ").lower() == 'yes'
    usenumbers = input("Would you like to include numbers? (yes/no): ").lower() == 'yes'
    usesymbols = input("Would you like to include symbols? (yes/no): ").lower() == 'yes'
    excludesimilar = input("Would you like to exclude similar characters? (yes/no): ").lower() == 'yes'
    numpasswords = int(input("How many passwords would you like to generate?: "))

    if useletters or useuppercaseletters or usenumbers or usesymbols:
        charactertypes['letters'] = charactertypes['letters'] if useletters else ''
        charactertypes['uppercaseletters'] = charactertypes['uppercaseletters'] if useuppercaseletters else ''
        charactertypes['numbers'] = charactertypes['numbers'] if usenumbers else ''
        charactertypes['symbols'] = charactertypes['symbols'] if usesymbols else ''

        if excludesimilar:
            charactertypes['letters'] = charactertypes['letters'].replace('l', '').replace('I', '').replace('1', '').replace('o', '').replace('O', '').replace('0', '')
            charactertypes['uppercaseletters'] = charactertypes['uppercaseletters'].replace('I', '')
            charactertypes['numbers'] = charactertypes['numbers'].replace('1', '').replace('0', '')
            charactertypes['symbols'] = charactertypes['symbols'].replace('I', '').replace('l', '').replace('1', '').replace('o', '').replace('O', '').replace('0', '')

        passwords = []
        for _ in range(numpasswords):
            password = generatepassword(length, charactertypes)
            passwords.append(password)
            print("Generated Password:", password)
            print("Strength:", calculatestrength(password))
            print()

        savetofile = input("Would you like to save these passwords to a file? (yes/no): ").lower() == 'yes'
        if savetofile:
            filename = input("Enter the file name (e.g., passwords.txt): ")
            with open(filename, 'w') as f:
                f.write('\n'.join(passwords))
                print("Passwords saved to", filename)
    else:
        print("No character types selected. Please select at least one.")

if __name__ == "__main__":
    main()
