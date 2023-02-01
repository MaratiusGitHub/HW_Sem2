# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

n = int(input('введите число n: '))
result = 1
if n == 1:
    print(result)
elif n <= 0:
    print('Вы ввели некорректные данные')
else:
    while result <= n:
        print(result)
        result *= 2
