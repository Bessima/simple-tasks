'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

'''

digits = input().split()
current_position = 0
last_position = len(digits)-1
if not last_position:
    print(digits[0])
    exit()

new_list = []
for elem in digits:

    if current_position == 0:
        prev = int(digits[last_position])
    else:
        prev = int(digits[current_position-1]) if current_position-1 >= 0 else 0

    if current_position == last_position:
        next = int(digits[0])
    else:
        next = int(digits[current_position+1]) if current_position < last_position else 0

    new_list.append(str(prev + next))

    current_position += 1

print(' '.join(new_list))
