#First create two separate functions so the code will look clean
#In the first function create the check_guess and store the guess, and secret number
#Write if/elif/else to define the value of the guessed number with secret_number
#In the second function add the main content, import random, add while, write try and except for valueerror handling, create result to check the number. 
#check the guess number is matching the secret number or is it high or low and print appropritae response with the if/elif/else - the entered number is high, low, correct and return the value.
#In the end call the function play_game()
def check_guess(guess, secret):
#pass #I'll fill this later
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    else:
        return "correct"


def play_game():
    import random
    number = random.randint(1, 10)
    while True:
        try:
            guess_number = int(input("Enter a number from 1 to 10: "))
            result = check_guess(guess_number, number)
            if result == "low":
                print("The number is low, try again")
            elif result == "high":
                print("The number is high, try again")
            else:
                print("The number is correct, you won")
                break

        except ValueError:
            print("Invalid value, enter a correct value in the given range.")

play_game()



