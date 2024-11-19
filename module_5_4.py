class House:
    # Атрибут класса для хранения истории
    houses_history = []

    def __new__(cls, *args, **kwargs):
        """
        Метод __new__ вызывается перед __init__.
        Добавляет название объекта в историю.
        """
        # Добавляем название дома (первый аргумент args) в историю
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        """
        Метод инициализации объекта класса House.
        :param name: Название дома.
        :param number_of_floors: Количество этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        """
        Метод __del__ вызывается при удалении объекта.
        """
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        """
        Метод перемещения на указанный этаж.
        :param new_floor: Этаж, на который нужно переместиться.
        """
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """
        Магический метод для получения количества этажей.
        :return: Количество этажей (self.number_of_floors).
        """
        return self.number_of_floors

    def __str__(self):
        """
        Магический метод для строкового представления объекта.
        :return: Строка в формате "Название: <название>, кол-во этажей: <этажи>".
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

# Проверка истории
print(House.houses_history)

# Удаление последнего объекта
del h1
