import time

# множества

# q = {'a', 'f', 1, 1, 2, 3, 25, (2, 5)}
# print(q)


# y = set()
# print(y)



# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#     return list_new

# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))

# start = time.time()
# result = f(z, x, c)
# stop = time.time() - start

# print(stop)



# z2 = list(range(10000))
# x2 = list(range(5000, 15000))
# c2 = list(range(10000, 20000))

# start2 = time.time()


# r = set(z2)
# t = r.union(set(x2), set(c2))
# stop2 = time.time() - start2
# list = list(t)


# print(stop2)
# print(type(list))


# =========================================================
# методы множеств
# z = {1,2,3,4,5}
# x = {3,4,5,6,7}
# q = {11}

# z.add(6)                            # добавить в множество элемент
# z.discard(6)                        # удалить элемент (если нет, ошибки не возникает)
# z.remove(6)                         # удалить элемент (если нет, возникает ошибка)
# y = z.union(z, x)                   # обьединить множества
# z.update(x, q)                      # обьединить множества
# y = z.intersection(x)               # определить пересечения множеств(общие элементы)
# y = z.difference(x)                 # определить разницу множеств(какие в множест Z невстречаются в X)



# print(y)


# ============================================================
# пример
new = set()

r = open('/home/dm/bin/test_110.txt')
new.update(set(r.read().split()))

print(new)

r.close()








