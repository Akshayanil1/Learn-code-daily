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


# print("\n___Library Inventory___")
# print(book1)
# book1.check_out()
# print(book1)
# book1.return_book()
# print(book1)
# print("\n___End of Library Inventory___")

class Library:
    def __init__(self, initial_books=None):
        self.books = initial_books if initial_books else []
        print("Library created. Shelves are empty.")
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added '{title}' by {author} to the library.")
        
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")
        print("---------------------\n")

book1 = Book("Ajaya Roll of the Dice", "Ananda Neelakantan")
book2 = Book("The Alchemist", "Paulo Coelho")

my_library = Library(initial_books=[book1, book2])

my_library.add_book("Ponniyin Selvan", "Kalki Krishnamurthy")
my_library.add_book("Sivagamiyin Sabatham", "Kalki Krishnamurthy")

my_library.display_books()

first_book = my_library.books[0]
print(f"Cheking out teh fisrt book: '{first_book.title}'...")
first_book.check_out()
my_library.display_books()
