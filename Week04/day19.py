#Module 02
# Task 1
# 99 Bottles of Beer
for i in range(99, 0, -1):
    print(f"{i} bottle{'s' if i != 1 else ''} of beer")

# Task 2
# Todo list
todos = ["Complete python module 2", "Do workout for 30 minutes", "Practice coding"]
for task in todos:
    print(task)

# Task 3
# The annoying parrot
while True:
    user_input = input("Enter a value: ")
    if user_input == "quit":
        break
    print(f"Parrot repeats: {user_input}")
print("You shut the parrot's mouth, successfully")

# Task 4
# The Number guessing game
import random
number = random.randint(1, 10)
while True:
    try:
        guess_number = int(input("Guess from 1 to 10: "))
        if guess_number < number:
            print("The number is low, try again")
        elif guess_number > number:
            print("The number is high, try again")
        else:
            print("The number you guessed is correct, you won")
            break
    except ValueError:
        print("Invalid input enter a number in the given range.")

#Module 03
# Task 1
# The Greeter
def greet():
    print("Hello! welcome to the world of functions")
greet()
greet()
greet()

# Task 2
# The Personalized Greeter
def greet_user(name):
    print(f"Hello! {name} welcome to the world of functions")
greet_user("Dhoni")
greet_user("Sachin")
greet_user("Kohli")

# Task 3
# The Adder - A Tool That Gives Back
def add_numbers(x, y):
    result = x + y
    return result
sum_result = add_numbers(10, 20)
print(sum_result)

# Task 4
# Refactor Your Guessing Game

def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"
def play_game():
    import random
    number = random.randint(1, 10)
    while True:
        try:
            guess_number = int(input("Guess from 1 to 10: "))
            result = check_guess(guess_number, number)
            if result == "low":
                print("The number is low, try again")
            elif result == "high":
                print("The number is high, try again")
            else:
                print("The number you guessed is correct, you won")
                break
        except ValueError:
            print("Invalid input enter a number in the given range.")

play_game()

# Module 4
# Task 1 : The Personal Profile

my_profile = {
   # "key" : "value"
    "name" : "Akshay",
    "age" : 27,
    "current_job" : "Virtual_Assistant",
    "target_job" : "Software_Developer"
}
print(my_profile["name"])

# Task 2: Modifying Your World

my_profile["skills"] = ["Python", "Problem Solving"]
my_profile["current_job"] = "Junior Developer"
del my_profile["target_job"]
print(my_profile)

# Task 3: Looping Through a Dictionary

for key,value in my_profile.items():
    print(key, value) 

# Task 4 (CHALLENGE): A Simple Contact Book

contact_book = []

def add_contact(name, phone, email):
    contact_book.append ({
        "name" : name,
        "phone" : phone,
        "email" : email
    })
def display_contacts():
    if not contact_book:
        print("No contact found")
    else:
        for contact in contact_book:
            print(f"Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}")

name = input("Enter contact name: ")
phone = input("Enter contact phone: ")
email = input("Enter contact email: ")
add_contact(name, phone, email)
# print(contact_book)
display_contacts()
