# # Module 1

# # This is an age calculator,
# # which will tell you how many years left for you to reach 100 years old 
# # or how many years passed since you turned 100 years old. 100 - age.
# # it will use basic if/elif/else and try, except fo valueerror handling.

# try:
#     age = int(input("Enter your age: "))
#     if age <= 0 or age >150:
#         print("Enter a reasonable age between 1 to 150")
#     else:
#         years_left = 100 - age
#         if years_left > 0:
#             print(f"You have {years_left} for you to turn 100!")
#         elif years_left == 0:
#             print(f"Congratulations you are turning 100 years old this year!")
#         else:
#             print(f"You have turned 100 years old {-years_left} years ago")
#         print()
# except ValueError:
#     print("Invalid input please enter a valid age as a number.")

# # This a madlib generator, which will ask user for input and based on a pre set statement it will generate some content
# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")
# adjective = input("Enter an adjective: ")

# print(f"The {adjective} {noun} {verb} in the library")

# # This is a calculator, which calculate total bill amount with the tip.
# amount = float(input("Enter the bill amount: "))
# tip = float(input("Enter the tip percentage(ex. 7, 8.5, 12): "))

# tip_amount = amount * tip/100
# total_amount = amount + tip_amount

# print(f"Bill Amount: {amount:.2f}")
# print(f"Tip %: {tip:.2f}")
# print(f"Tip Amount: {tip_amount:.2f}")
# print(f"Total Amount: {total_amount:.2f}")

# # This program will ask you some question, based on your answers it will suggest what can you
# while True:
#     age = int(input("Enter your age: "))
#     if age >= 25 and age != 150:
#         print("You are old enough to rent a car in India.")
#         print("You are old enough to drink in India.")
#         print("You are eligible to vote.")
#     elif age >= 21 and age != 150:
#         print("You are old enough to drink in India.")
#         print("You are eligible to vote.")
#     elif age >= 18 and age != 150:
#         print("You are eligible to vote.")
#     elif age >= 150:
#         print("Invalid input try again")
#     else:
#         print("You are too young, focus on your studies and enjoy your youth!")
#     break

# # Module 2
# # This program will print 99 bottles of beer, 98, 97 .. till the set limit, using the for loop
# for i in range(99, 0, -1):
#     print(f"{i} bottle{'s' if i != 1 else ''} of beer")

# # The parrot will repeat what ever the user say till the user say quit. so it will annoy the user till he quit.
# while True:
#     user_input = input("Enter a word: ")
#     if user_input == "quit":
#         break
#     else:
#         print(f"The parrot repeats: {user_input}")

# # Lets play the classing number guessing game.
# # ask for user to enter a number but before that store the secret number and then match the entered number.
# # now whether it matches or not if not tell the user either it is low, high and print correct if the entered number matches the secret code.
# import random
# number = random.randint(1, 10)
# while True:
#     try:
#         guess_number = int(input("Enter a number b/w 1 to 10: "))
#         if guess_number > number:
#             print("It is high, try again")
#         elif guess_number < number:
#             print("It is low, try again")
#         else:
#             print("correct, you won!")
#             break
#     except ValueError:
#         print("invalid input, try again")

# # Module 3
# # Lets greet the user first with the help of the function
# def greet(name):
#     print(f"hello {name}, welcome to function!")
# greet("Akshay")

# # Now lets do some basic maths with the help of the function, also this time we will use return instead of print
# def add_numbers(x, y):
#     result = x + y
#     return result

# sum_result = add_numbers(10, 20)
# print(sum_result)

# # Now lets refactor our guessing game with the help of functions.
# # now we will create two set of functions one will ddefine the value high, low, correct.
# # the other one will do the other guessing part with the random and guess number.
# def check_guess(guess, secret):
#     if guess < secret:
#         return "low"
#     elif guess > secret:
#         return "high"
#     else:
#         return "correct"
# def play_guess():
#     import random
#     number = random.randint(1, 10)
#     while True:
#         try:
#             guess_number = int(input("Enter a number b/w 1 to 10: "))
#             result = check_guess(guess_number, number)
#             if result == "low":
#                 print("number is low, try again")
#             elif result == "high":
#                 print("number is high, try again")
#             else:
#                 print("number is correct, you won!")
#                 break
#         except ValueError:
#             print("invalid input, try again")
# play_guess()

# Module 4
my_profile = {
    "name" : "abc",
    "age" : 29,
    "current_job" : "bpo",
    "target_job" : "developer"
}
print(my_profile["name"])
print(my_profile)

# updated my_profile
my_profile["skills"] = ["python", "problem solving"]
my_profile["current_job"] = ["junior developer"]
del my_profile ["target_job"]
print(my_profile) 

# looping through key, value using for:
for key, value in my_profile.items():
    print(key, value)

# to the final challenge a contact book, integrating functions, using dictionary and list
contact_book = []

def add_contacts(name, phone, email):
    contact_book.append ({
    "name" : name,
    "phone" : phone,
    "email" : email
    })
def display_contact():
    if not contact_book:
        print("no contact found")
    else:
        for contact in contact_book:
            print(f"Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}")

name = input("Enter your name: ")
phone = input("Enter your phone: ")
email = input("Enter your email: ")
add_contacts(name, phone, email)
display_contact()