class House:
    def __init__(self, name, number_of_floors):
        """
        Метод инициализации объекта класса House.
        :param name: Название дома.
        :param number_of_floors: Количество этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

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
h2 = House('ЖК Акация', 20)

# Использование __str__
print(h1)
print(h2)

# Использование __len__
print(len(h1))
print(len(h2))
