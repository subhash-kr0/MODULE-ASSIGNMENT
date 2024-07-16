class LibraryBook:
    def __init__(self, book_name, author):
        self._book_name = book_name
        self._author = author
        self._available = True

    # Getter methods
    def get_book_name(self):
        return self._book_name

    def get_author(self):
        return self._author

    def is_available(self):
        return self._available

    # Borrow the book
    def borrow_book(self):
        if self._available:
            print(f"{self._book_name} by {self._author} has been borrowed.")
            self._available = False
        else:
            print(f"{self._book_name} is currently not available.")

    # Return the book
    def return_book(self):
        if not self._available:
            print(f"{self._book_name} has been returned.")
            self._available = True
        else:
            print(f"{self._book_name} was not borrowed.")

# Example usage
book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald")
book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee")

# Borrow and return books
book1.borrow_book()
book2.borrow_book()

book1.return_book()
book2.return_book()
