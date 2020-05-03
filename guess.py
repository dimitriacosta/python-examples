#!/usr/local/bin/python3
# This program is a game to guess a random number
import random
import sys

# print('Hello. What is your name?')
name = input('Hello. What is your name? ')

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secret = random.randint(1,20)
legend = 'You lost'

guesses = []

for attempt in range(1,7):
    # print('Take a guess')
    try:
        guess = int(input('Take a guess: '))
    except ValueError:
        print('You did not enter a number')
        sys.exit(1)

    if guess < secret:
        print("You're to low")
        guesses.append(guess)
    elif guess > secret:
        print("You're too high")
        guesses.append(guess)
    else:
        legend = 'You won'
        break

print(legend + ' and it took you ' + str(attempt) + ' attempts.')
