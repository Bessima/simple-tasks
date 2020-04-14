"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""

a, b, c = int(input()), int(input()), int(input())
min = 0
max = 0
if a >= b:
    max = a
    if c > a:
        max = c
        min = b
        print(max)
        print(min)
        print(a)
    elif a > c and b > c:
        min = c
        print(max)
        print(min)
        print(c)
        print(b)
    else:
        min = b
        print(max)
        print(min)
        print(c)
else:  # b>a
    max = b
    if c > b:
        max = c
        min = a
        print(max)
        print(min)
        print(b)
    elif b > c and a > c:
        min = c
        print(max)
        print(min)
        print(a)
    else:
        min = a
        print(max)
        print(min)
        print(c)
