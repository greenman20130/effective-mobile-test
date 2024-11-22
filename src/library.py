import json
from book import Book

class Library:
    def __init__(self):
        self.books = self._load_books()

    def _load_books(self):
        try:
            with open('books.json', 'r') as file:
                books_data = json.load(file)
                return [Book(**book_data) for book_data in books_data]
        except FileNotFoundError:
            return []

    def _save_books(self):
        books_data = [vars(book) for book in self.books]
        with open('books.json', 'w') as file:
            json.dump(books_data, file)

    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year, "в наличии")
        self.books.append(new_book)
        self._save_books()

    def remove_book(self, book_id):
        book_to_remove = next((book for book in self.books if book.id == book_id), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self._save_books()
        else:
            print("Книга с указанным id не найдена.")

    def search_books(self, query):
        return [book for book in self.books if query.lower() in (book.title.lower() + book.author.lower() + str(book.year))]

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год издания: {book.year}, Статус: {book.status}")

    def change_book_status(self, book_id, new_status):
        book_to_change = next((book for book in self.books if book.id == book_id), None)
        if book_to_change:
            book_to_change.status = new_status
            self._save_books()
        else:
            print("Книга с указанным id не найдена.")