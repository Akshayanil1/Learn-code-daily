# # Module 5: The Mission
# # Task 1: Creating Your Digital Footprint
# with open ("day20.txt", "w") as file:
#     file.write("Hello World!!")
# # Task 3: Appending to History
# with open ("day20.txt", "a") as file:
#     file.write("\nBye World!!")
# # Task 2: Reading the Record
# with open ("day20.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Task 4 (CHALLENGE): Your Persistent Contact Book
# contact_book = []

# def add_contact(name, phone, email):
#     with open ("contacts.txt", "a") as file:
#         file.write(f"{name}, {phone}, {email}\n")
#     contact_book.append({"name": name, "phone": phone, "email": email})
# def load_contacts():
#     try:
#         with open("contacts.txt", "r") as file:
#             for line in file:
#                 name, phone, email = line.strip().split(",")
#                 contact_book.append({"name": name, "phone": phone, "email": email})
#     except ValueError:
#         print("No contacts found yet. starting with an empty file")
# load_contacts()
# name = input("Enter contact name: ")
# phone = input("Enter contact phone: ")
# email = input("Enter contact email: ")
# add_contact(name, phone, email)
# print(contact_book)

# contact_book = []
# def add_contact(name, phone, email):
#     with open("contact.txt", "a") as file:
#         file.write(f"{name}, {phone}, {email}\n")
#     contact_book.append({"name": name, "phone": phone, "email": email})
# def view_contact():
#     try:
#         with open("contact.txt", "r") as file:
#             for line in file:
#                 name, phone, email = line.strip().split(",")
#                 contact_book.append({"name": name, "phone": phone, "email": email})
#     except FileNotFoundError:
#         print("No file found")
# view_contact()
# name = input("Enter contact name: ")
# phone = input("Enter contact phone: ")
# email = input("Enter contact email: ")
# add_contact(name, phone, email)

# print(contact_book)
FILENAME = "CONTACT.txt"
def load_contacts():
    contact_book = []
    try:
        with open (FILENAME, "r") as file:
            for line in file:
                if line.strip():
                    name, phone, email = line.strip().split(",")
                    contact_book.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip()})
    except FileNotFoundError:
        # print("No file found, lets start with a new file")
        pass
    return contact_book
def save_contacts(name, phone, email):
    with open (FILENAME, "a") as file:
        file.write(f"{name}, {phone}, {email}\n")
def display_contacts(contact_list):
    print("\n--- Your Contacts ---")
    if not contact_list:
        print("Your contact book is empty")
    else:
        for i,contact in enumerate(contact_list):
            print(f"{i+1}. Name: {contact["name"]}, Phone: {contact["phone"]}, email: {contact["email"]}")  
def run_program():
    # will righ later
    my_contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_contacts(my_contacts)
        elif choice == "2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ") 
            new_contact = {"name": name, "phone": phone, "email": email}
            my_contacts.append(new_contact)
            save_contacts(name, phone, email)
            print(f"'{name}' has been added.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")

run_program()   