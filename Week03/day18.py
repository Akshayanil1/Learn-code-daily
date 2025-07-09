#task:0
# Age calcluator
#This program calculates how many years are left until the user turns 100 years old.100 - age

try:
    age = int(input("Enter your age: "))
    
    if age <= 0 or age > 150:
        print("Please enter a realistic age between 0 to 150.")
    else:
        years_left = 100 - age
        if years_left > 0:
            print(f"You have, {years_left} years left until you turn 100 years old 🎉")
        elif years_left == 0:
            print("Congratulations you are turning 100 years old this year! 🎉")
        else:
            print(f"You turned 100 years old {-years_left} years ago! 🎉")
        
except ValueError:
    print("Invalid input. Please enter a valid age as a number.")

# task:1  
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

print(f"The {adjective} {noun} {verb} in the library")

#task:2

# import math
    
amount = float(input("Enter the bill amount: "))
tip = float(input("Enter the tip percentage(ex. 15, 7.5, 18): "))

tip_amount = amount * (tip/100)
total_amount = (amount + tip_amount)
# rounded_total = round(total_amount)

print(f"Bill amount: {amount:.2f}")
print(f"Tip percentage: {tip:.2f}%")
print(f"Tip amount: {tip_amount:.2f}")
print(f"Total bill: {total_amount:.2f}")

#task:3

age = int(input("Enter your age: "))

# if age >= 25:
#     print("You are eligible to vote.")
# if age >= 21:
#     print("You are old enough to drink in India.")
# if age >= 18:
#     print("You are old enough to rent a car in India.")
# if age < 18:
#     print("You are still young, focus on your studies and enjoy your youth!")

if age >= 25:
    print("You are old enough to rent a car in India.")
    print("You are old enough to drink in India.")
    print("You are eligible to vote.")
elif  age >= 21:
    print("You are old enough to drink in India.")
    print("You are eligible to vote.")
elif age >= 18:
    print("You are eligible to vote.")
else:
    print("You are still young, focus on your studis and enjoy your youth!")