# TODO: описать базовый класс
class Animal:
    """
    Базовый класс Animal (Животное).
    
    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        species (str): Вид животного.
    
    Методы:
        __init__: Конструктор для инициализации объекта.
        __str__: Возвращает строковое представление объекта.
        __repr__: Возвращает строку для внутреннего представления объекта.
        make_sound: Базовый метод для издания звука.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Animal.

        Параметры:
            name (str): Имя животного.
            age (int): Возраст животного.
            species (str): Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.

        Возврат:
            str: Строка с информацией о животном.
        """
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def __repr__(self) -> str:
        """
        Возвращает строку для внутреннего представления объекта Animal.

        Возврат:
            str: Строка с форматом для дебаггинга.
        """
        return f"Animal(name='{self.name}', age={self.age}, species='{self.species}')"

    def make_sound(self) -> str:
        """
        Метод, который возвращает базовый звук животного.

        Возврат:
            str: Строка со звуком животного.
        """
        return "Some generic animal sound"


# TODO: описать дочерний класс
class Dog(Animal):
    """
    Дочерний класс Dog, наследующий Animal.

    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        species (str): Вид животного (устанавливается автоматически как "dog").
        breed (str): Порода собаки.
    
    Методы:
        __init__: Расширяет конструктор базового класса.
        __str__: Перегружает строковое представление.
        make_sound: Перегружает метод для издания звука.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.

        Параметры:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age, "dog")  # Устанавливаем вид "dog" через базовый класс.
        self.breed = breed

    def __str__(self) -> str:
        """
        Перегружает строковое представление объекта Dog.

        Возврат:
            str: Строка с информацией о собаке.
        """
        return f"{self.name} is a {self.age}-year-old {self.breed} dog."

    def make_sound(self) -> str:
        """
        Перегружает метод make_sound для класса Dog.

        Возврат:
            str: Строка со звуком собаки.
        """
        return "Woof! Woof!"


# Пример использования:
if __name__ == "__main__":
    generic_animal = Animal(name="GenericAnimal", age=5, species="unknown")
    dog = Dog(name="Buddy", age=3, breed="Golden Retriever")

    print(generic_animal)  # GenericAnimal is a 5-year-old unknown.
    print(dog)  # Buddy is a 3-year-old Golden Retriever dog.
    print(dog.make_sound())  # Woof! Woof!