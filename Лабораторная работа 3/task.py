class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        """
        Инициализация базового класса книги.

        :param name: Название книги.
        :param author: Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """
        Свойство для получения названия книги.
        Название книги нельзя изменить.
        """
        return self._name

    @property
    def author(self):
        """
        Свойство для получения имени автора.
        Имя автора нельзя изменить.
        """
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает строку, которая позволяет однозначно идентифицировать объект.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация бумажной книги.

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц книги.
        """
        super().__init__(name, author)
        self.pages = pages  # Установка значения через setter

    @property
    def pages(self):
        """
        Свойство для получения количества страниц.
        """
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """
        Свойство для установки количества страниц с проверкой значений.

        :param value: Новое значение количества страниц.
        :raises TypeError: Если переданное значение не является целым числом.
        :raises ValueError: Если количество страниц меньше или равно нулю.
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self):
        """
        Возвращает строковое представление бумажной книги.
        """
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        """
        Возвращает строку, которая позволяет однозначно идентифицировать бумажную книгу.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"
        )


class AudioBook(Book):
    """Класс для аудиокниг."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация аудиокниги.

        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность аудиокниги в часах.
        """
        super().__init__(name, author)
        self.duration = duration  # Установка значения через setter

    @property
    def duration(self):
        """
        Свойство для получения продолжительности аудиокниги.
        """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Свойство для установки продолжительности с проверкой значений.

        :param value: Новое значение продолжительности аудиокниги.
        :raises TypeError: Если переданное значение не является числом.
        :raises ValueError: Если продолжительность меньше или равна нулю.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = value

    def __str__(self):
        """
        Возвращает строковое представление аудиокниги.
        """
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    def __repr__(self):
        """
        Возвращает строку, которая позволяет однозначно идентифицировать аудиокнигу.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
        )