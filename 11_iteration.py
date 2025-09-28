import random
# iteration
# вычислимые последовательности, обьект должен иметь встроеный метод __next__ 
# enumerate

# e = enumerate("ERW")
# print(list(e))                                                      # [(0, 'E'), (1, 'R'), (2, 'W')]
# print(list(e))                                                      # []

# e = enumerate("ASD")
# print(next(e))                                                      # (0, 'A')
# print(next(e))                                                      # (1, 'S')
# print(next(e))                                                      # (2, 'D')
# print(next(e))                                                      # StopIteration

# e = enumerate("ASD")
# print(e.__next__())                                                 # (0, 'A')
# print(e.__next__())                                                 # (1, 'S')
# print(e.__next__())                                                 # (2, 'D')
# print(e.__next__())                                                 # StopIteration
# --------------------------------------------------------------------------------------
#zip
# z = zip("ASD", range(1,4))
# print(next(z))                                                        # ('A', 1)
# print(next(z))                                                        # ('S', 2)
# print(next(z))                                                        # ('D', 3)
# print(next(z))                                                        # StopIteration
# --------------------------------------------------------------------------------------
# map - применяяет заданную функцию к последовательности 
# e = map(int, "123 456 798 ".split())                                # (применяем функцию int к последовательности)
# print(next(e))                                                      # 123
# print(list(e))                                                      # [456, 798]
# --------------------------------------------------------------------------------------
# filter 
# e = filter(lambda x: x%3, range(1,14))
# print(list(e))
# --------------------------------------------------------------------------------------
# сделать строку итератором (получить итератор из итерируемого обьекта) если у него есть встроеный метод iter (dir"QWE")
# e = iter("QWE")
# print(next(e))                                                        # Q
# print(next(e))                                                        # W
# print(next(e))                                                        # E
# --------------------------------------------------------------------------------------
# вызываем функцию, пока она не вернет стоп значение(3)
# d = iter(lambda: random.randrange(5), 3)
# print(list(d))
# ======================================================================================
# ======================================================================================
# ======================================================================================
# Генераторы
# e = (i * 2 + 1 for i in range(3))
# print(next(e))                                                          # 1
# print(next(e))                                                          # 3
# print(next(e))                                                          # 5
# print(next(e))                                                          # StopIteration

# --------------------------------------------------------------------------------------
# print(list(i % 15 for i in range(7,14)))
# print(sorted(i % 15 for i in range(7,14)))
# print(sorted((i % 15 for i in range(7,14)), key=str))

# --------------------------------------------------------------------------------------
# Генераторы функции (при повторном вызове, продолжает выполнение где была прошлая остановка на yield)

# def gen(n):
#     for i in range(n):
#         yield i+1
# res = gen(3)
# print(res)                                                              # вернет генератор, который можно будет использовать
# print(next(res))                                                        # 1
# print(next(res))                                                        # 3
# print(next(res))                                                        # 5
# --------------------------------------------------------------------------------------
# из гениратора вызывает еще один гениратор
# def g1(n):
#     yield n
#     yield n + 1
# def g2(x):
#     yield 3
#     yield from g1(x)
#     yield 4
# print(list(g2(10)))                                                     # [3, 10, 11, 4]
# --------------------------------------------------------------------------------------
# Параметрические генераторы. передаем параметры для yield (первый запуск next(p) как бы "инициализация", дальше передаем параметры)
# def pgen(x):
#     res = yield x
#     print("res1:", res)
#     res = yield res + x
#     print("res2:", res)
#     res = yield res * x
# p = pgen(10)
# print(p)
# print(next(p))
# print(p.send(100))                                  # 100 отправляем в res
# print(p.send(2))                                    # 2 отправляем в res
# --------------------------------------------------------------------------------------
# # пример, return из итератора и yield from
# def gen(x):
#     yield from x
#     return len(x)

# def runner(g):
#     res = yield from g
#     print("Result", res)

# g = gen("qwe")
# res = runner(g)
# print(next(res))                                                 # q
# print(next(res))                                                 # w
# print(next(res))                                                 # e
# print(next(res))                                                 # Result 3
# ======================================================================================
# def fun():
#     yield "One"
#     yield "Two"
# def run():
#     yield from fun()
#     yield from fun()
# for i in run():
#     print(i)
# ======================================================================================
# def subr(n):
#     yield f"One: {n}"
#     yield f"Two: {n}"
#     return f"Done: {n}"

# def task():
#     for i in range(3):
#         result = yield from subr(i)
#         yield result
#     return "*END*"

# core = task()
# try:
#     while (res := next(core)):
#         print(res)
# except StopIteration as E:
#     print(E.value)
# ======================================================================================
# def task(initial):
#     value = initial
#     while True:
#         value = yield f"<{value * 2}>"

# core = task(100500)
# print(f"Start: {next(core)}")
# for i in range(5):
#     print(core.send(i + 1))
# ======================================================================================
# def subr():
#     x = yield "Wait for x"
#     y = yield f"Wait for y ({x=})"
#     return x, y

# def task():
#     while True:
#         value = yield from subr()
#         _ = yield value

# core = task()
# print(next(core))
# for i in range(8):
#     print(core.send(i))
# ======================================================================================
def mult():
    x = yield "Give me X"
    y = yield "Give me Y"
    return x * y
def task():
    while True:
        res = yield from mult()
        res2 = yield res
        print("Got", res2)
core = task()
next(core)
for i in range(1, 10):
    print(core.send(i))

# ======================================================================================
# https://docs.python.org/3/library/itertools.html
from itertools import *
# Itertools
# count
# C = count(10, 2)                                                  # 10 с шагом 2, безконечный, считает пока есть что считать
# for a, b in zip("QWER", C):
#     print(a, b)
# --------------------------------------------------------------------------------------
# accumulate (плюсует предыдущее значение)
# print(list((range(5))))                                             # [0, 1, 2, 3, 4]
# print(list(accumulate(range(5))))                                   # [0, 1, 3, 6, 10]
# print(list(accumulate(range(7))))                                   # [0, 1, 3, 6, 10, 15, 21]
# print(list(accumulate(range(1, 7), int.__mul__)))                   # [1, 2, 6, 24, 120, 720]
# --------------------------------------------------------------------------------------
# batched (разбивает элементы) python3.12
# print(list(range(16)))                                              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(list(batched(range(16), 4)))                                  # [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)]
# --------------------------------------------------------------------------------------
# pairwise()
# print(list(pairwise("1234")))                                        # [('1', '2'), ('2', '3'), ('3', '4')]
# --------------------------------------------------------------------------------------
# islice()
# for e in islice("QWERQWERQWE", 3, 100, 2):                             # R->W->R->W (третий элемент с шагом 2)
    # print(e)
# --------------------------------------------------------------------------------------






