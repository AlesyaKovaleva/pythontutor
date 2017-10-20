# -*- coding: utf8 -*-

# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (пробелы важны!).

number = int(input())
next_number = number + 1
previous_number = number - 1
print('The next number for the number ' + str(number) + ' is ' + str(next_number) + '.')
print('The previous number for the number ' + str(number) + ' is ' + str(previous_number) + '.')
