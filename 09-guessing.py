## Todo list:
### Catch the value error if user inputs a string instead of int.

import random
number = random.randint(1, 100)
# Print intro/rules here, can copy from v4 code
print("Welcome to the guessing game!")
print("\nI'm thinking of a number between 1 and 100 for you to guess.")
print("\nIf you guess within 10 of the number i'll tell you you're warm. If not, i'll tell you cold.")
print("\nIf your next guess is closer than the last, i'll tell you warmer. If not, i'll tell you colder.")
print("\nGood luck!")
guesses = []
while True:
    guess = int(input("\n\nGuess a number between 1 - 100:\n"))
    guesses += [guess]
    if guess == number:
        break
#Put warmer/colder code below. Nest the loop. find way to avoid warm/cold elifs and replace with warmer/colder loop instead
    elif len(guesses) > 1:
        if abs(number - guesses[-2]) > abs(number - guess):
            print("\n\nYou're warmer! Guess again.")
        else:
            print("\n\nYou're colder, guess again.")
#Above code needs to be placed in right order to check old guess vs new and still run before warm/cold loop
    elif guess > 100 or guess < 1:
        print("\n\nOut of range number! Guess again using 1 - 100 only.")
    elif abs(number - guess) < 11:
        print("\n\nYou're warm! Guess again.")
    elif abs(number - guess) > 10:
        print("\n\nYou're cold, guess again.")

if len(guesses) == 1:
    print(f"\n\n\nYou guessed correctly, the number was {number} and it only took you a single guess to get it right, what luck! Great job!")
else:
        print(f"\n\n\nYou guessed correctly, the number was {number} and it took you {len(guesses)} guesses to get it right. Great job!")
