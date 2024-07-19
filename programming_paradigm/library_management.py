class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False
        
    def returnBook(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False
        
    def __str__(self):
        return f"${self.title} by {self.author}"
    
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, newBook):
        for book in self._books:
            if book.title == newBook.title and book.author == newBook.author:
                return False
            else:
                self._books.append(newBook)
                return True


    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.checkout()
                return True
            else:
                return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out:
                book.returnBook()
                return True
            else:
                return False

    
    def list_available_books(self):
        for allBooks in self._books:
            if not allBooks._is_checked_out:
                print(allBooks)
