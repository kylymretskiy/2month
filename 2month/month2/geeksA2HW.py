# 1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры).
# 2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта.
# 3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры).
# 4. Добавить в класс Figure нереализованный публичный метод info (вывод полной информации о фигуре).
# 5. Создать класс Square (квадрат), наследовать его от класса Figure.
# 6. Добавить в класс Square атрибут side_length (длина одной стороны квадрата), атрибут должен быть приватным.
# 7. В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.
# 8. В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом:
# Например - Square side length: 5cm, area: 25cm.
# 9. Создать класс Rectangle (прямоугольник), наследовать его от класса Figure.
# 10. Добавить в класс Rectangle атрибуты length (длина) и width (ширина), атрибуты должны быть приватными.
# 11. В классе Rectangle переопределить метод calculate_area, который бы считал и возвращал площадь прямоугольника.
# 12. В классе Rectangle переопределить метод info, который бы распечатывал всю информацию о прямоугольнике следующим образом:
# Например - Rectangle length: 5cm, width: 8cm,  area: 40cm.
# 13. В исполняемом файле (в запускаемой области модуля) создать список из 2-х разных квадратов и 3-х разных прямоугольников.
# 14. Затем через цикл необходимо вызвать у всех объектов списка метод info.
# 15. Установить программу git на свой ПК, зарегистрироваться на github.com и создать новый репозиторий, в котором у вас будут храниться все домашние задания.
#  16. Залить ДЗ 2 в созданный репозиторий и прикрепить ссылку на ваш репозиторий на платформу https://online.geeks.kg/

class Figure:
    unit = "cm"

    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        area = self.calculate_area()
        print(f'Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}.')

class Rectangle(Figure):
    def __init__(self, width, length):
        super().__init__()
        self.__width = width
        self.__length = length

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width:{self.__width}{self.unit},  area: {area}{self.unit}")

figures_list = [
    Square(2),
    Square(9),
    Rectangle(5,6),
    Rectangle(7,8),
    Rectangle(9,10),
]

for i in figures_list:
    print(i.info())

    
