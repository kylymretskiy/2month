# 1. Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию
# 4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию.


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

spisok = [ 2 , 6, 9, 3 , 4 , 8 , 7 ]
bubbleSort(spisok)
print(spisok)


def binary_search(val , arr):

    ResultOk = False
    First = 0
    Last = len(arr) - 1
    Pos = -1
    while First<Last:
        Middle = (First + Last) // 2
        if val == arr[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            Pos = Middle
            break
        elif val > arr[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk == True:
        print("Элемент найден.")
        return Pos
    else:
        print("Элемент не найден.")
        return -1

spisok = [2, 3, 4, 6, 7, 8, 9]
element = 6
result = binary_search(element, spisok)

if result != -1:
    print(f"Элемент {element} найден на позиции {result}.")
else:
    print(f"Элемент {element} отсутствует.")



