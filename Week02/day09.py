# def user_greeting(name):
#     print(f"Hello, {name}! Welcome to our program.")
# user_greeting("Alice")
# user_greeting("Bob")

# user_input_name = input("What is your name? ")
# user_greeting(user_input_name)

# def calculate_area(width, height):
#     area = width * height
#     return area

# rectangle1_area = calculate_area(5, 10)
# rectangle2_area = calculate_area(3, 7)

# print(f"Area of rectangle 1: {rectangle1_area}")
# print(f"Area of rectangle 2: {rectangle2_area}")

# total_area = rectangle1_area + rectangle2_area

# print(f"Total area of both rectangles: {total_area}")

def calculate_total_bill(bill_amount, tip_percentage):
    
    tip_amount = bill_amount * (tip_percentage/100)
    grand_total = bill_amount + tip_amount
    return grand_total


bill_amount = float(input("Enter the bill amount: $ "))
tip_percentage = float(input("Enter the tip percentage you want to give: "))

final_bill = calculate_total_bill(bill_amount, tip_percentage)

print(f"The total bill amount including tip is: $ {final_bill:.2f}")