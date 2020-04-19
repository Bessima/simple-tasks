'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())

first_line_index = a-1
first_column_index = c-1
column = 0
for line in range(first_line_index, b+1):
    print_str = ''
    if column == 0:
        print_str = '\t'
        column += 1
        for i in range(c, d+1):
            print_str += str(i) + '\t'
    else:
        for j in range(first_column_index, d+1):
            if j == first_column_index:
                print_str += str(line) + '\t'
                continue
            print_str += str(j*line) + '\t'
    print(print_str)
