

error = 'Введите правильное значение'

sequence_numbers = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))

#######################################################################
# Функция для определения цифр в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

#########################################################################
# Проверка соответствия указанному в условии ввода данных.

if " " not in sequence_numbers:
    print("\nВ ВВОДЕ ОТСУТСТВУЮТ ПРОБЕЛЫ (введите числа, согласно условиям ввода.)")
    sequence_numbers = input('Введите целые числа через пробел: ')
if not is_int(sequence_numbers):
    print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите числа, согласно условиям ввода.)\n')
    print(error)
else:
    sequence_numbers = sequence_numbers.split()

########################################################################
# Меняем список строк на список чисел

list_sequence_numbers = [int(item) for item in sequence_numbers]

########################################################################
# Сортировка списка

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

##############################################################
list_sequence_numbers = merge_sort(list_sequence_numbers)
##############################################################
# Установка позиции элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

##################################################################
# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.

print(f'Упорядоченный по возрастанию список: {list_sequence_numbers}')

