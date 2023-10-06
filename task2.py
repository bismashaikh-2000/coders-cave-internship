# task 3
# Random Password Generator Application

import random
import string

# Define the character sets for the password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special_characters = '@!#&*_'
all_characters = lower + upper + numbers + special_characters

# Welcome dashboard
try:
    print("   ┌─────────────────────────────────────────────────┐")
    print("   │ WELCOME TO THE RANDOM PASSWORD GENERATOR        │")
    print("   └─────────────────────────────────────────────────┘")

    print(''' 
    GUIDELINES:
    - Choose the length of your password.
    - The password can include uppercase letters, digits, and special characters.
    - You can customize the complexity of your password.

    Let's generate a password to enhance your security!!\n''')

    # Ask the user for password complexity
    print("What kind of password complexity are you comfortable with?\n- Strong\n- Moderate\n- Weak")

    # loop if the user enter the invalid input
    while True:
        pass_strength = input('Enter your desired complexity: ').lower()

        if pass_strength == 'strong':
            print('For Strong Passwords: Password length should be greater than 8.')
            break

        elif pass_strength == 'moderate':
            print('For Moderate Passwords: Password length range must be between (6-8).')
            break

        elif pass_strength == 'weak':
            print('RISK!!\nWeak passwords are easy to hack...Choose carefully.')
            print('For Weak Passwords: Password length should be less than 6.')
            break

        else:
            print('Invalid Input!!')

    # For the length of the password entered by the user
    # loop for if length is not under the condition required by user
    while True:
        pass_length = int(input("Enter the desired password length: "))

        if pass_strength == 'strong' and pass_length <= 8:
            print('Length must be greater than 8')
            continue

        elif pass_strength == 'moderate' and not (6 <= pass_length <= 8):
            print('Length range must be between (5-8)')
            continue

        elif pass_strength == 'weak' and pass_length >= 6:
            print('Length must be less than 6')
            continue

        if pass_length <= 0:
            print("Password length must be greater than zero.")

        else:
            password = ''
            for pasw in range(pass_length):
                password += random.choice(all_characters)

            # Generate and display the password
            print(f'Generated Password: {password}')
            print('Congratulations! Your password has been created.')

            # Check the strength and print the complexity and password
            strength = "Weak"
            if len(password) >= 9:
                strength = "Strong"
            elif len(password) >= 6:
                strength = "Moderate"

            print(f'Password Strength: {strength}')
            print('Thanks for using!')
            break

# exception handling
except ValueError:
    print("Invalid input!! Please enter a valid number.")