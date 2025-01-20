from random import randint
def game(cash , first_number , last_number, attempts):
    while attempts > 0:
        if cash <= 0:
            print("Вы бомж")
            break
        print(f"Кол-во попыток: {attempts}")
        print( f'Your capital: {cash}')
        random_number = randint(first_number , last_number)
        stavka = int(input("Ваша ставка: "))
        if 0 < stavka <= cash:
            print("Ваша ставка принята!")
        else:
            print(f"Введите ставку только от 1 до {cash}!")
            continue
        user_number = int(input(f"Выберите число от {first_number} до {last_number}: "))
        if user_number == random_number:
            cash += stavka * 2
            print(f'Вы выиграли! Ваш счет: {cash}')
        elif user_number < 1 or user_number > 10:
            print(f"Вводите числа только от {first_number} до {last_number}!")
            continue
        else:
            cash -= stavka
            print(f'Вы проиграли! Ваш счет: {cash}')
        attempts -= 1
