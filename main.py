import random


def guess(x):
    random_number = random.randint(1, x)
    guessing_number = 0
    while guessing_number != random_number:
        guessing_number = int(input(f'Guess a number between 1 and {x}: '))
        print(guessing_number)
        if guessing_number < random_number:
            print("Sorry guess again. Too low")
        elif guessing_number > random_number:
            print("Sorry, guess again. Too high.")
    return print(f"Yay, congrats. You have just guessed the number {random_number}")


guess(10)
