# 1. Создать класс Person с атрибутами full_name, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса base_salary.
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.

class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"Меня зовут {self.full_name}, мне {self.age} лет, и я {'женат(а)' if self.is_married else 'не женат(а)'}."

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        return sum(self.marks.values())/len(self.marks)

class Teacher(Person):
    base_salary = 45000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        else:
            bonus = 0
        return Teacher.base_salary + bonus



teacher_person = Teacher('aleksey',25,'yes',4)
print(teacher_person.introduce_myself())
print(f'Зарплата: {teacher_person.salary()}')

def create_students():
    student1 = Student('kylym' , 17, False, {'математика': 5, 'русский': 4, 'литература': 4} )
    student2 = Student('artur' , 18, False, {'математика': 4, 'русский': 5, 'литература': 4} )
    student3 = Student('migel' , 18, False, {'математика': 4, 'русский': 4, 'литература': 5} )
    return [student1 , student2 , student3]

students = create_students()
for student in students:
    print(student.introduce_myself())
    for subject, mark in student.marks.items():
        print(f'{subject}: {mark}')
    print(f'Средняя оценка: {student.average_mark()}')