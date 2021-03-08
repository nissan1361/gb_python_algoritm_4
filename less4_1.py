# Проанализировать скорость и сложность одного любого алгоритма 
# из разработанных в рамках домашнего задания первых трех уроков

import timeit
import cProfile

# Взял 8 задачу урока 2

number = input("Введите число: ")
num1 = input("Введите искомую цифру: ")

def firstfunc():
    count = 0
    for num in number:
        if num == num1:
            count = count + 1
    return count
print("Искомая цифра встречается {} раз!".format(firstfunc()))

cProfile.run('firstfunc()')

# Вариант 2:

num_string = str(number)
def sec_func():
    counter = num_string.count(num1)
    return counter

print("Искомая цифра (Вар 2) встречается {} раз!".format(sec_func()))

cProfile.run('sec_func()')

# Первый вариант эффективнее!