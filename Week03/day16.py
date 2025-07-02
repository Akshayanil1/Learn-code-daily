
# try:
#     age = int(input("Enter your age: "))
#     print(f"Next year, you will be {age + 1} years old.")
# except ValueError:
#     print("Enter a valid input in number.")
# else:
#     print(f"You entered {age}")
# finally:
#     print("Thank you for using the age callculator.")

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    operation = input("Enter teh operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
    else:
        print("Invalid operation! Please choose +, -, *, or /.")
        continue
    break
