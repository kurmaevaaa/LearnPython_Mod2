from task_1 import Book, Car, Laptop  # Импортируем созданные ранее классы

if __name__ == "__main__":
    # Создание объектов классов
    book = Book("Python Basics", 300)
    car = Car("Toyota", 50, 10)
    laptop = Laptop("Dell", 50)

    # Проверка обработки ошибок через try...except
    try:
        book.read(-10)  # Некорректное количество страниц
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        car.refuel(-5)  # Некорректное количество топлива
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        laptop.charge(-5)  # Некорректное количество заряда
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        laptop.power_on()  # Попытка включить ноутбук с разряженной батареей
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке