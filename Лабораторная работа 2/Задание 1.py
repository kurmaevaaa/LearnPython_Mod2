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

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
