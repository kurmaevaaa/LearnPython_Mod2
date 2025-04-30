BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO: написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        # Инициализация атрибутов книги
        self.id = id_ # Идентификатор книги (целое число)
        self.name = name # Название книги (строка)
        self.pages = pages # Количество страниц в книге (целое число)

    def __str__(self):
        # Метод для пользовательского строкового представления книги
        # Возвращает строку в формате: Книга "название_книги"
        return f'Книга "{self.name}"'

    def __repr__(self):
        # Метод для представления объекта в виде строки, пригодной для создания экземпляра
        # Возвращает строку в формате: Book(id_=идентификатор, name='название', pages=количество_страниц)
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
# TODO: написать класс Library
class Library:
    """
    Класс для представления библиотеки.

    Атрибуты:
        books (list): Список объектов класса Book.

    Методы:
        get_next_book_id(): Возвращает идентификатор для добавления новой книги.
        get_index_by_book_id(book_id): Возвращает индекс книги по её id.
    """

    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        Параметры:
            books (list, optional): Список объектов Book. По умолчанию - пустой список.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор книги.

        Если библиотека пуста, возвращает 1.
        Если книги есть, возвращает id последней книги + 1.

        Returns:
            int: Следующий идентификатор книги.
        """
        if not self.books:  # Если список книг пуст
            return 1
        return self.books[-1].id + 1  # id последней книги + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её id.

        Параметры:
            book_id (int): Идентификатор книги.

        Returns:
            int: Индекс книги в списке.

        Вызывает:
            ValueError: Если книги с таким id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
