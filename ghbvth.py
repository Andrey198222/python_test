# Функция сортировки (метод пузырька) списка по возрастанию элементов в нем:
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Функция проверки ввода целого положительного числа, в границах интервала (< input_number <=):
def digit_check(list, low, high):
    try:
        input_number = int(input(f'\n>> Введите число, которое  > {list[low]} и <= {list[high]} : '))
        if not (list[low] < input_number <= list[high]):
            raise ValueError
    except ValueError:
        print("\033[31m<< Введенное число не попадает в границы массива! >>\033[37m")
        input_number = digit_check(list, low, high)
    return input_number

# Функция двоичного поиска:
def binary_search(list, number, low, high):

    middle = len(list) // 2
    while list[middle] != number and low <= high:
        if number > list[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (low + high) // 2

    if low > high:
        return middle
    else:
        return middle-1

# На вход подается последовательность чисел через пробел, преобразование введённой последовательности в список:
my_list = list(map(int, input("\n>> Введите массив чисел через пробел  : ").split()))

# Определяем граничные индексы:
my_low = 0
my_high = len(my_list)-1

# Сортировка списка:
my_list = bubble_sort(my_list)
print("\nОтсортированный список введенных чисел:", my_list)

# Запрашивается у пользователя любое число из граничных значений отсортированного списка:
my_number = digit_check(my_list, my_low, my_high)

# Осуществляется двоичный поиск номера позиции элемента (индекс в отсортированном списке),
# который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# и выводится результат:
my_index = binary_search(my_list, my_number, my_low, my_high)

print("\n\033[32m>> Номер позиции элемента списка равен:\033[37m", my_index,
      ", \033[32mэлемент равен:\033[37m", my_list[my_index])

Footer
