class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализация объекта класса House.
        :param name: Название дома.
        :param number_of_floors: Количество этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        """
        Возвращает количество этажей.
        """
        return self.number_of_floors

    # Методы сравнения
    def __eq__(self, other):
        """
        Проверяет равенство количества этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        """
        Проверяет неравенство количества этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __lt__(self, other):
        """
        Проверяет, меньше ли количество этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        """
        Проверяет, меньше или равно количество этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        """
        Проверяет, больше ли количество этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        """
        Проверяет, больше или равно количество этажей.
        """
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    # Методы арифметических операторов
    def __add__(self, value):
        """
        Увеличивает количество этажей на значение value.
        """
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        """
        Увеличивает количество этажей на значение value (обратный порядок аргументов).
        """
        return self.__add__(value)

    def __iadd__(self, value):
        """
        Увеличивает количество этажей на значение value (для операции +=).
        """
        return self.__add__(value)


# Тестирование
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # False

h1 = h1 + 10  # __add__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # __iadd__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # __radd__
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False
