# number = float(input("Enter a number: "))

# square = number ** 2
# cube = number ** 3

# print(f"""
#       The square of {number} is {square}.
#       The cube of {number} is {cube}.
# """)

# print("--- End of program ---")

print("Welcome to KFC Pizza!")

slices_per_pizza = 8
print(f"Slices Per Pizza: {slices_per_pizza}")

number_of_pizzas = int(input("""How many pizzas would you like to order? 
Enter the number of pizzas: """))
total_people = int(input("""How many people are there at the party? 
Enter the people count: """))

total_slices = number_of_pizzas * slices_per_pizza
slices_per_person = total_slices // total_people
remaining_slices = total_slices % total_people
print(f"Total pizzas ordered: {number_of_pizzas}")
print(f"Total people at the party: {total_people}")
print(f"Total slices of pizzas: {total_slices}")
print(f"Slices per person: {slices_per_person}")
print(f"Remaining slices of pizza: {remaining_slices}")

print("Thank you for ordering with KFC Pizza!")
print("--- End of program ---")