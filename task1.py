# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

firstNumber = int(input('Введите любое число: '))
secondNumber = int(input('Введите степень числа: '))

def power(firstNumber, secondNumber):
    if secondNumber == 0:
        return 1
    return firstNumber * power(firstNumber, secondNumber - 1)

number = power(firstNumber, secondNumber)

print(f'A = {firstNumber}; B = {secondNumber} -> {number}')