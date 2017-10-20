# -*- coding: utf8 -*-

# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
# Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести
# искомое количество яблок (два числа).

schoolkids = int(input())
apples = int(input())
apples_to_schoolkids = apples // schoolkids
apples_in_basket = apples % schoolkids
print(apples_to_schoolkids)
print(apples_in_basket)
