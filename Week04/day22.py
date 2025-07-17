# OOPS Python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        print(f"New book created: '{self.title}' by {self.author}.")

    def __str__(self):
        if self.is_checked_out:
            status = "Checked out"
        else:
            status = "On Shelf"
        return f"'{self.title}' by {self.author} - (Status: {status})"

    def check_out(self):
        print(f"Checking out '{self.title}'..")
        self.is_checked_out = True
    
    def return_book(self):
        print(f"Returning '{self.title}'..")
        self.is_checked_out = False


book1 = Book("Ajaya Roll of the Dice", "Ananda Neelakantan")
book2 = Book("The Alchemist", "Paulo Coelho")

print("\n___Library Inventory___")
print(book1)
book1.check_out()
print(book1)
book1.return_book()
print(book1)
print("\n___End of Library Inventory___")
# ...existing code...