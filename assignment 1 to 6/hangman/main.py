import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left. Used letters:", ' '.join(used_letters))
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died. The word was", word)
    else:
        print("Yay! You guessed the word", word)

hangman()
