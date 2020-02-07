""""Hangman game where user can input a word and another user can try to guess the word in 10 attempts.
The user can enter one letter at a time, not alpha characters are not allowed. The user can not guess a letter
twice. When the word is guessed correctly the user gets feedback and the program breaks."""

import re
import time

word_to_guess = input("Please enter a word: ")

# Handle exception when user entered no alpha
while not word_to_guess.isalpha():
    print("Only alphabetic letters please")
    word_to_guess = input("Please enter a word: ")

# Define globals
guess_counter = 10
guess_letters_str = ""
empty_dots = len(word_to_guess) * "."
empty_dots_lst = list(empty_dots)
guessed_letters = ""

# Create a loop where guess counter get decremented every time when the user gives a letter.
while guess_counter != 0:
    guess_counter -= 1
    guess_letter = input("Please enter one letter: ")

    # Handle exception when user enters no alpha
    while not guess_letter.isalpha():
        print("That is not a letter, please insert a letter")
        guess_letter = input("Please enter one letter: ")

    # Handle exception when there is more than 1 char in the guess
    while len(guess_letter) > 1:
        print("Enter just one letter please")
        guess_letter = input("Please enter one letter: ")

    # Handle exception when the letter is already guessed and don't decrement amount of guesses
    while guess_letter in guessed_letters:
        print("You have already guessed this letter, try again.")
        guess_letter = input("Please enter one letter: ")

    guessed_letters += guess_letter
    guess_letters_str += guess_letter

    # If the guessed letter is not in the word to guess ask for input again
    if guess_letter not in word_to_guess:
        print("Nope, this letter is not in the word, try again")
        print("Guesses left:", guess_counter)

    # If the guessed letter is in the word to guess find the index(es) and give feedback
    if guess_letter in word_to_guess:
        indexes = ([x.start() for x in re.finditer(guess_letter, word_to_guess)])
        print("Yes this letter is in the word, good job")
        print("Guesses left:", guess_counter)

        # replace empty dots with the guessed letter that is in the word to guess
        for i in indexes:
            empty_dots_lst[i] = word_to_guess[i]
        joined_empty_dots_lst = "".join(empty_dots_lst)
        print(joined_empty_dots_lst)

        # If the word is guessed give feedback and end script with break to jump out the loop
        if joined_empty_dots_lst == word_to_guess:
            print("Well done you guessed right")
            # Add sleep time for terminal presentation
            time.sleep(60)
            break

    # Handle guesses when they are zero and break
    if guess_counter == 0:
        print("You are out of guesses, better luck next time!")
        # Add sleep time for terminal presentation
        time.sleep(60)
        break