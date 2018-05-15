#Imports
import random

print('----------------------------\n      Guess the number\n----------------------------\n')

# Generating a random number
number = random.randint(0, 100)
guess = -1

# Ask for player's name
name = input('Hi player, what is your name ? ')

while guess != number:

    # Now, we ask the user to input a random number between 0 and 100 and convert it into an integer
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    # Checking if number and guess are equals.
    if guess > number:
        print('Sorry {}, your guess of {} is too high, try again'.format(name, guess))
        guess_text
    elif guess < number:
        print('Sorry {}, your guess of {} is too low, try again'.format(name, guess))
        guess_text
    else:
        print('Congratulations {}, the correct number was {}. Good job!'.format(name, guess))
