# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся
# в каждом из трех классов.

class_1 = int(input())
class_2 = int(input())
class_3 = int(input())
desks_1 = (class_1 // 2) + (class_1 % 2)
desks_2 = (class_2 // 2) + (class_2 % 2)
desks_3 = (class_3 // 2) + (class_3 % 2)
total = desks_1 + desks_2 + desks_3
print(total)
