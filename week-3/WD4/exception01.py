from random import randint

def get_integer():
    number = int(input("Enter an integer: "))
    return number

number_to_guess = randint(0,10)
number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("You entered a wrong value.")
    else:
        if guess > number_of_guesses:
            number_of_guesses -= 1
            print("You entered a too high number.")
        if guess < number_of_guesses:
            number_of_guesses -= 1
            print("You entered a too small number.")
        elif guess == number_to_guess:
            print("Your number is matching. Congratulations!")
            break

if number_of_guesses == 0:
    print("The number was: %d." % number_to_guess)
