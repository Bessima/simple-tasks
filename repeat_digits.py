'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

digits = input().split()
digits.sort()

value = digits[0]
uniq = []

for digit in digits[1:]:
    if digit == value:
        if digit in uniq:
            continue
        uniq.append(digit)
    else:
        value = digit

print(' '.join(uniq))
