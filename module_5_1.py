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


# Создание объектов класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to с разными этажами
h1.go_to(5)
h2.go_to(10)
