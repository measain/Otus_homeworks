list_cube = list()                  # пустой список для последующего добавления в него квадратов аргументов переданных в функцию

def power_numbers(*chislo):         # использую "*", так как неизвестно количество аргументов, которые будут передаваться в функцию
    for i in chislo:
        list_cube.append(i **2)      # в конце каждой итерации цикла в конец списка list_cube добавляется результат вычисления квадрата числа
    return list_cube                # после всех итераций происходит вывод итогового списка на экран

print('Kvadrat peredannyh chisel:', power_numbers(3,2,4))
print()
print('----------')

# ------------------------------------------------------------------------------

# filter types
ODD = "Нечетное"
EVEN = "Четное"
PRIME = "Простое"


def filter_numbers(numbers, type):
    result = []                       # создал пустой список, в который будут попадать отфильтрованные числа
    if type == ODD:                   # условие проверки нечетности
        for i in numbers:
            if i % 2 == 1:            # если делится с остатоком - нечетное, попадает в список result
                result.append(i)
    if type == EVEN:                  # условие проверки четности
        for i in numbers:
            if i % 2 == 0:            # если делится без остатка - четное, попадает в список result
                result.append(i)
    if type == PRIME:                 # условие проверки на простое число
        for i in numbers:
            d = 2
            while i % d != 0:         # уловие делит переданные в функции числа на d+1 до тех пор, пока в остатке не останется 0
                d += 1
            if i == d:                # если 0 в остатке был получен при делении числа на такое же число - число попадает в список result
                result.append(i)
    return result

print()
print('Nechetnye:', filter_numbers(list(range(2, 20)), ODD))
print('CHetnye:', filter_numbers(list(range(2, 20)), EVEN))
print('Prostye:', filter_numbers(list(range(2, 20)), PRIME))
