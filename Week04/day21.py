# Module 6 - OOPS:
# Task 1: The Blueprint - Your First Class
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
# Task 2: Making Objects Do Things - Methods   
    def bark(self):
        print(f"{self.name} says Woof!")
# Task 3: The String Representation
    def __str__(self):
        return f"Dog (name = {self.name}, age = {self.age}, color = {self.color})"

my_dog = Dog("Chopper", 4, "Blonde")
print(my_dog)
print(my_dog.name)
print(my_dog.age)
print(my_dog.color)
my_dog.bark()

# Task 4 (CHALLENGE): The OOP Contact Book
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
class ContactManager:
    FILENAME = "contacts.txt"

    def __init__(self):
        self.contacts = []
        self.load_contacts()
    def load_contacts(self):
        try:
            with open(self.FILENAME, "r") as file:
                for line in file:
                    if line.strip():
                        name, phone, email = line.strip().split(",")
                    self.contacts.append(Contact(name, phone, email))
        except FileNotFoundError:
            print("No contacts found. Starting with empty contact book.")
    def save_contacts(self):
        with open (self.FILENAME, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")
    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for i, contact in enumerate(self.contacts, start = 1):
                print(f"{i}. {contact}")
    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added succesfully.")
    def run(self):
        while True:
            print("\nContact Book Menu: ")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                self.add_contact(name, phone, email)
            elif choice == "2":
                self.display_contacts()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. please try again.")
if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
        
