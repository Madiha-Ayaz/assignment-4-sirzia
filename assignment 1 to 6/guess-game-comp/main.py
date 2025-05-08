import random

def computer_guess():
    print("Welcome to the Guess the Number Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    
    low = 1
    high = 100
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one possible choice
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number correctly: {guess}!")
        else:
            print("Please enter 'H' for high, 'L' for low, or 'C' for correct.")

# Start the game
computer_guess()
