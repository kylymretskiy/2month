# Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список сим-карт)
# 5. Добавить сеттеры и геттеры к существующему атрибуту.
# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию построения маршрута до локации.
# 9. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.
# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 12. Распечатать информацию о созданных объектах.
# 13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы).
# 14. В репозитории вашего проекта с дз удалить папки .idea, .venv и __pycache__
# 15. Создать файл .gitignore и вписать в него ненужные папки для репозитория

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Getters and setters
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, value):
        self.__cpu = value

    def get_memory(self):
        return self.__memory

    def set_memory(self, value):
        self.__memory = value

    # Method for computations
    def make_computations(self):
        return self.__cpu + self.__memory

    # Magic methods
    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Getters and setters
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards):
        self.__sim_cards_list = sim_cards

    # Method for making calls
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Calling {call_to_number} using SIM-{sim_card_number}: {sim_card}")
        else:
            print("Invalid SIM card number.")

    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Building a route to {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()})"


# Creating objects
computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom", "O! Mobile"])
smartphone1 = SmartPhone(cpu=8, memory=64, sim_cards_list=["Beeline", "O! Mobile"])
smartphone2 = SmartPhone(cpu=6, memory=32, sim_cards_list=["MegaCom"])

# Printing object information
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Testing methods
print("\nTesting Computer methods:")
print(f"Make computations: {computer.make_computations()}")

print("\nTesting Phone methods:")
phone.call(1, "+996777998811")
phone.call(3, "+996555667788")

print("\nTesting SmartPhone methods:")
smartphone1.call(2, "+996550112233")
smartphone1.use_gps("Ala-Too Square")

print("\nTesting comparison operators:")
print(f"smartphone1 > smartphone2: {smartphone1 > smartphone2}")
print(f"smartphone1 == smartphone2: {smartphone1 == smartphone2}")
print(f"smartphone1 < smartphone2: {smartphone1 < smartphone2}")