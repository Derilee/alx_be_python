class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for newBook in self.books:
            if newBook.title == book.title and newBook.author == book.author:
                return False
            else:
                self.books.append(book)
                return True


    def list_books(self):
        for allBooks in self.books:
            if isinstance(allBooks, EBook):
                print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}")
            elif isinstance(allBooks, PrintBook):
                print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")
            else:
                print(f"Book: {self.title} by {self.author}")
