
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».

# Второй — без использования «Решета Эратосфена».

# 1 вариант: "решето Эратосфена"


import timeit
import cProfile

def sieve(i):
    n = i * 20

    sieve_ = [k for k in range(n)]
    sieve_[1] = 0

    for k in range(2, n):
        if sieve_[k] != 0:
            j = k + k
            while j < n:
                sieve_[j] = 0
                j += k

    # print(sieve_)
    # print([i for i in sieve_ if i != 0])

    array = [k for k in sieve_ if k != 0]
    # print(array)
    # print(len(array))
    return array[i - 1]

print(sieve(1_000))

# 2 вариант: без "решета"

def prime(i):

    n = i * 20
    prime_ = []
    for k in range(2, n + 1):
        for j in prime_:
            if k % j == 0:
                break
        else:
            prime_.append(k)
    return prime_[i - 1]

print (prime(1_000))

print(timeit.timeit('sieve(10)', number=100, globals=globals())) # 0.013413000000000008
print(timeit.timeit('sieve(100)', number=100, globals=globals())) # 0.1364165
print(timeit.timeit('sieve(200)', number=100, globals=globals())) # 0.27902669999999996
print(timeit.timeit('sieve(500)', number=100, globals=globals())) # 0.7024697000000001
# print(timeit.timeit('sieve(1_000)', number=100, globals=globals())) # 1.4391881999999998

print(timeit.timeit('prime(10)', number=100, globals=globals())) # 0.012562999999999658
print(timeit.timeit('prime(100)', number=100, globals=globals())) # 0.5365245000000001
print(timeit.timeit('prime(200)', number=100, globals=globals())) # 1.6994036000000001
print(timeit.timeit('prime(500)', number=100, globals=globals())) # 8.297358899999999
# print(timeit.timeit('prime(1_000)', number=100, globals=globals())) # 30.641805500000004

# В варианте №1 (решето Эратосфена) наблюдается более-менее линейная сложность О(n) (возможно, логарифмическая). 
# Во втором варианте зависимость квадратичная О(n ** 2), поэтому на больших значениях
# этот алгоритм значительно медленнее.

cProfile.run('sieve(1000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.028    0.028 <string>:1(<module>)
#         1    0.024    0.024    0.028    0.028 task_4_2.py:16(sieve)
#         1    0.001    0.001    0.001    0.001 task_4_2.py:19(<listcomp>)
#         1    0.003    0.003    0.003    0.003 task_4_2.py:32(<listcomp>)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(1000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.316    0.316 <string>:1(<module>)
#         1    0.315    0.315    0.316    0.316 task_4_2.py:41(prime)
#         1    0.000    0.000    0.316    0.316 {built-in method builtins.exec}
#      2262    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
