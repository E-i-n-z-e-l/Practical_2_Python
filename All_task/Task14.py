# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


number_N = int(input('Введите число N '))
while number_N <= 1:
    print('Введите положительное число и не "1" ')
    number_N = int(input('Введите число N '))

count = 1
degree = 0
while count < number_N:
    if 2**degree < number_N:
        print(2**degree)
    degree = degree + 1
    count = count + 1