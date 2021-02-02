# 1. Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# 2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

# вариант 1: через рекурсию

DENOM = - 2

def summ(num, n):
    if n == 1:
        return num
    else:
        return num + summ((num / DENOM), (n - 1))

# n = int(input('Введите количество элементов ряда: '))
# num = 1
# sum_ = summ(num, n)
#
# print(sum_)

print(timeit.timeit('summ(1, 10)', number=100, globals=globals())) # 0.00035500000000000115
print(timeit.timeit('summ(1, 100)', number=100, globals=globals())) # 0.0036278000000000005
print(timeit.timeit('summ(1, 200)', number=100, globals=globals())) # 0.0073036
print(timeit.timeit('summ(1, 500)', number=100, globals=globals())) # 0.0203667

# cProfile.run('summ(100)')

# вариант 2: через цикл

# n = int(input('Введите количество элементов ряда: '))

def func_1(n):
    num = 1
    sum_ = 0

    for i in range(n):
        sum_ = sum_ + num
        num = num / DENOM

print(timeit.timeit('func_1(10)', number=100, globals=globals())) # 0.00025089999999999835
print(timeit.timeit('func_1(100)', number=100, globals=globals())) # 0.0015712999999999977
print(timeit.timeit('func_1(200)', number=100, globals=globals())) # 0.0030945
print(timeit.timeit('func_1(500)', number=100, globals=globals())) # 0.008518600000000001
print(timeit.timeit('func_1(100_000)', number=100, globals=globals())) # 2.2139429

cProfile.run('func_1(100_000)')

# print(sum_)

# вариант 3: с массивом

# n = int(input('Введите количество элементов ряда: '))

def func_2(n):
    num = 1
    array = []
    for i in range(n):
        array.append(num)
        num = num / DENOM
# print(array)
    sum_ = sum(array)

print(timeit.timeit('func_2(10)', number=100, globals=globals())) # 0.00028210000000000734
print(timeit.timeit('func_2(100)', number=100, globals=globals())) # 0.0018862999999999935
print(timeit.timeit('func_2(200)', number=100, globals=globals())) # 0.004220199999999993
print(timeit.timeit('func_2(500)', number=100, globals=globals())) # 0.0102405
print(timeit.timeit('func_2(100_000)', number=100, globals=globals())) # 2.3362901

cProfile.run('func_2(100_000)')

# print(sum_)

# Вывод: все три алгоритма имеют линейную сложность O(n). Быстрее всех работает алгоритм №2,
# несколько отстаёт от него алгоритм №3. Рекурсивный алгоритм №1 - самый медленный.
