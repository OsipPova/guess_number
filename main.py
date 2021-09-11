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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_comp = random.randint(low, high)
        else:
            guess_comp = low # could also be high because low = high
        feedback = input(f'Is {guess_comp} too high (H), too low (L), or correct(C)?? ').lower()
        if feedback == 'h':
            high = guess_comp - 1
        elif feedback == 'l':
            low = guess_comp + 1

    print(f'Yay! The computer guessed your number, {guess_comp}, correctly!')

computer_guess(10)