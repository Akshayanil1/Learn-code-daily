# Contact Manager OOP
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
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        contacts = []
        # Attempt to read contacts from file
        try:
            with open(self.FILENAME, "r") as file:
                contacts = []
                for line in file:
                    if line.strip():
                        name, phone, email = line.strip().split(",")
                        contacts.append(Contact(name.strip(), phone.strip(), email.strip()))
        
        except FileNotFoundError:
            print("No contacts found, starting with an empty contact book.")
        return contacts
    
    def save_contacts(self):
        with open(self.FILENAME, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name}, {contact.phone}, {contact.email}\n")

    def run_program(self):
        while True:
            print("\n--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                email = input("Enter contact email: ")
                new_contact = Contact(name, phone, email)
                self.contacts.append(new_contact)
                print(f"Contact '{new_contact.name}' saved successfully.")
            elif choice == "2":
                if not self.contacts:
                    print("No contacts available.")
                else:
                    for i, contact in enumerate(self.contacts, start=1):
                        print(f"{i + 1}. {contact}")
            elif choice == "3":
                self.save_contacts()
                print("Contacts saved. Good bye!")
                break
            else:
                print("Invalid choice, please try again.")
if __name__ == "__main__":
    manager = ContactManager()
    manager.run_program()

# Contact Manager OOP