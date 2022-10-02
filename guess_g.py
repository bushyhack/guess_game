# This is a guess game
import random

number_0f_guesses = 0
random_number = random.randint(1,10)
player = (input("What's your name? "))
print(f"Welcome {player.title()}. Now guess a number between 1 and 10")

while number_0f_guesses < 3:
    guess = int(input())
    number_0f_guesses += 1
    if guess < random_number:
        print("Number is too low!")
    if guess > random_number:
        print("Number is too high!")
    if guess == random_number:
        break

if guess == random_number:
    print(f"Congratulations {player.title()}. You rocked it!")
else:
    print(f"Hey {player}, don't give up yet!")

   