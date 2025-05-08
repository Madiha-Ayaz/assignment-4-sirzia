import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    num_passwords = int(input("How many passwords would you like to generate? "))
    length = int(input("Enter the desired password length: "))

    for i in range(num_passwords):
        print(f"Password {i+1}: {generate_password(length)}")
except ValueError:
    print("Please enter a valid number.")
