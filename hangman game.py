import random

#list of predefined word
words = ["python", "computer", "programming", "developer", "hangman"]

# Randomly choose word
word = random.choice(words)

#store guess letter
guessed_letters = []

#store number of attempt
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print(" Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess not in word:
        attempts -= 1
        print(" Wrong guess! Attempts left:", attempts)
    else:
        print(" Correct guess!")

# If user loses
if attempts == 0:
    print("\n Game Over! The word was:", word)