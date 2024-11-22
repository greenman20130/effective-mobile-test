from library import Library

def main():
    library = Library()

    while True:
        print("""Меню:
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Отображение всех книг
5. Изменение статуса книги
6. Выход""")

        choice = input("Введите номер операции: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
            print("Книга добавлена.")

        elif choice == "2":
            book_id = int(input("Введите id книги для удаления: "))
            library.remove_book(book_id)
            print("Книга удалена.")

        elif choice == "3":
            query = input("Введите запрос для поиска: ")
            found_books = library.search_books(query)
            if found_books:
                print("Результаты поиска:")
                for book in found_books:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год издания: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(input("Введите id книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии или выдана): ")
            library.change_book_status(book_id, new_status)
            print("Статус книги изменен.")

        elif choice == "6":
            print("Выход из приложения.")
            break

        else:
            print("Неверный номер операции. Попробуйте еще раз.")

if __name__ == "__main__":
    main()