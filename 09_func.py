import math

# def show():
#     print('функция')
# show()


# def show2():
#     x = 7
#     return x

# y = show2()
# z = show2() + 9

# print(z)
# print(show2())

# =================================================
# параметры и аргументы функции

# def count_list(x):
#     count = 0
#     for i in x:
#         count += 1
#     return count


# h = ['a', 'a', 'h']
# j = [9, 8, 7, 6]
# k = [9, 8, 7, 5, 7, 5]

# count = count_list(h)
# print(count)

# ====================================================

# def name(h, s, *args, key, mer):
#     print(h)
#     print(s)
#     print(args)
#     print(key)
#     print(mer)

# name(7, 8, 9, key=666, mer=777)

# ---------------------------------

# def exclusive_item(*args, key=False):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     if key == True:
#         new_list.sort()

#     return new_list





# z = [9, 8, 7]
# x = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5]


# t = exclusive_item(z, x, c, key=True)
# print('t:', t)

# ==============================================

# def name():
#     x = 100
#     name2(x)

# def name2(par):
#     print(par)

# name()


# ================================================

# x = 5

# def name():
#     x = 10
#     def name2():
#         nonlocal x
#         x = 200
#         print(x)

#     name2()
#     print(x)

# name()
# print(x)

# ================================================


PI = math.pi

def radius():
    n = float(input('Диаметр цилиндра в см: '))
    n /= 2
    return n

def heigth():
    m = float(input('Высота цилиндра в см: '))
    return m

def volume():
    r = radius()
    h = heigth()
    s = PI*r**2
    v = s*h
    return v

print(f'Обьем цилиндра: {volume()} см3')
















