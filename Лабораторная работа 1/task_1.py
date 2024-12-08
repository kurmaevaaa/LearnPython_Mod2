# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Car:
    """
    Класс, описывающий автомобиль.

    >>> car = Car("Toyota", 50, 10)
    >>> car.accelerate(20)
    >>> car.speed
    20.0
    >>> car.refuel(30)
    40.0
    >>> car.check_fuel()
    40.0
    """

    def __init__(self, brand: str, fuel_capacity: float, fuel_level: float):
        """
        Создаёт объект автомобиля.

        :param brand: Марка автомобиля.
        :param fuel_capacity: Ёмкость топливного бака (литры). Должна быть больше 0.
        :param fuel_level: Текущий уровень топлива (литры). Не может быть отрицательным и больше ёмкости бака.
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой.")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Ёмкость топливного бака должна быть положительным числом.")
        if not (0 <= fuel_level <= fuel_capacity):
            raise ValueError("Уровень топлива должен быть между 0 и ёмкостью бака.")

        self.brand = brand
        self.fuel_capacity = fuel_capacity
        self.fuel_level = float(fuel_level)
        self.speed = 0.0  # Начальная скорость

    def accelerate(self, increment: float = 10.0) -> None:
        """
        Увеличивает скорость автомобиля.

        :param increment: Прирост скорости (км/ч). Должен быть положительным.
        """
        if increment <= 0:
            raise ValueError("Прирост скорости должен быть положительным.")
        self.speed += float(increment)

    def refuel(self, amount: float) -> float:
        """
        Заправляет автомобиль топливом.

        :param amount: Количество топлива (литры). Должно быть положительным.
        :return: Остаток топлива в баке после заправки.
        """
        if amount <= 0:
            raise ValueError("Количество топлива для заправки должно быть положительным.")
        self.fuel_level = float(min(self.fuel_level + amount, self.fuel_capacity))
        return self.fuel_level

    def check_fuel(self) -> float:
        """
        Проверяет текущий уровень топлива.

        :return: Уровень топлива в баке (литры).
        """
        return float(self.fuel_level)

# TODO: описать ещё класс

class Laptop:
    """
    Класс, описывающий ноутбук.

    >>> laptop = Laptop("Dell", 50)
    >>> laptop.charge(30)
    80
    >>> laptop.power_on()
    >>> laptop.is_on
    True
    >>> laptop.power_off()
    >>> laptop.is_on
    False
    """

    def __init__(self, brand: str, battery_capacity: int):
        """
        Создаёт объект ноутбука.

        :param brand: Бренд ноутбука.
        :param battery_capacity: Ёмкость батареи (в %). Должна быть от 0 до 100.
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not (0 <= battery_capacity <= 100):
            raise ValueError("Ёмкость батареи должна быть в диапазоне от 0 до 100.")

        self.brand = brand
        self.battery_capacity = battery_capacity
        self.is_on = False  # Состояние ноутбука

    def power_on(self) -> None:
        """Включает ноутбук."""
        if self.battery_capacity == 0:
            raise ValueError("Невозможно включить ноутбук: батарея разряжена.")
        self.is_on = True

    def power_off(self) -> None:
        """Выключает ноутбук."""
        self.is_on = False

    def charge(self, amount: int = 10) -> int:
        """
        Заряжает ноутбук.

        :param amount: Процент заряда (по умолчанию 10%). Должен быть положительным.
        :return: Текущий уровень заряда батареи.
        """
        if amount <= 0:
            raise ValueError("Зарядка должна быть положительным числом.")
        self.battery_capacity = min(self.battery_capacity + amount, 100)
        return self.battery_capacity

# TODO: и ещё один

class Book:
    """
    Класс, описывающий книгу.

    >>> book = Book("Python Basics", 300)
    >>> book.read(50)
    50
    >>> book.progress()
    16.67
    >>> book.read(100)
    150
    >>> book.progress()
    50.0
    """

    def __init__(self, title: str, total_pages: int):
        """
        Создаёт объект книги.

        :param title: Название книги.
        :param total_pages: Общее количество страниц. Должно быть положительным.
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой.")
        if not isinstance(total_pages, int) or total_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.total_pages = total_pages
        self.current_page = 0  # Начальная страница

    def read(self, pages: int) -> int:
        """
        Читает заданное количество страниц.

        :param pages: Количество страниц для чтения. Должно быть положительным.
        :return: Текущая страница.
        """
        if pages <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным.")
        self.current_page = min(self.current_page + pages, self.total_pages)
        return self.current_page

    def progress(self) -> float:
        """
        Возвращает прогресс чтения книги в процентах.

        :return: Прогресс в процентах, округлённый до двух знаков после запятой.
        """
        return round((self.current_page / self.total_pages) * 100, 2)