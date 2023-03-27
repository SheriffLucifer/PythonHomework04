# Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

def addition(a, b):

    if b == 0:
        return a

    return addition(a + 1, b - 1)

sum = addition(a, b)
print(f'{a} + {b} = {sum}')