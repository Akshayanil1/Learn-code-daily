# age = int(input("Enter your age: "))

# if age < 18 and age > 0:
#     years_to_wait = 18-age
#     print(f"You are a minor. You have to wait for {years_to_wait} years to eligible to vote.")

# elif age >= 18 and age <= 130:
#     print("You are eligible to vote.")   
# else:
#     print("Invalid input. Please enter a valid age.")

# print("---- Program Finished ----")


user_name = input("Enter User Name: ")
user_password = input("Enter Password: ")

if user_name == "Admin" and user_password == "1234":
    print ("Access Granted")
elif user_name == "Admin" and user_password != "1234":
    print ("Incorrect Password")
elif user_name != "Admin" and user_password == "1234":
    print ("Incorrect User Name")
else:
    print ("Incorrect User Name and Password")
print("---- Program Finished ----")