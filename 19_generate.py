import os
h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5]

# new_h = []
# for x in h:
#     new_h.append(x*2)
# print(new_h)

# n = [x*2 for x in h]                                   # генератор списка
# print(n)
# # -----------------------------------------
# z = {x*2 for x in h}                                   #генератор множества
# print(z)
# # -----------------------------------------
# f = {x:x*2 for x in h}                                 #генератор словаря
# print(f)

# ===================================================

# new_h = []
# for x in h:
#     if x % 2 == 0:
#         new_h.append(x*2)
# print(new_h)

# g = [x*2 for x in h if x % 2 == 0]         # генератор списка с условием
# print(g)


# =====================================================

# new_h = []
# for x in h:
#     if x % 2 == 0:
#         new_h.append(x*2)
# print(new_h)

# g = [x*2 for x in h if x % 2 == 0 and x > 0]         # генератор списка с условием
# print(g)


# =====================================================

# g = [os.path.join(z, i) 
#     for z, x, c in os.walk('/home/dm/bin/') 
#     for i in c 
#     if '.txt' in i]

# print(g)

# =====================================================

# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# new_price = {}
# for i in price.keys():
#     new_price[i] = round(price[i] * 0.85, 2)
# print(new_price)

# # синтаксис генератора словарей
# new_d = {i:round(price[i] * 0.85, 2) for i in price.keys()}
# print(new_d)

# =====================================================

# выражение генератор

# h = ['https://www.youtube.com', 'https://www.root-me.org', 'https://habr.com', 'https://translate.google.com']

# n = [x.split('//')[1] for x in h if '.com' in x]
# # print(type(n))


# z = (x.split('//')[1] for x in h if '.com' in x)                        # выражение генератор

# # print(type(z))                # <class 'generator'>
# for i in z:
#     print(i)


# =====================================================

# n = [x for x in os.walk('/home/dm/bin/')]
# print('здесь')

# z = (y for y in os.walk('/home/dm/bin/'))
# print('тут')


# =====================================================
# функция генератор


# def some():
#     list_text = []
#     with open('text.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text


def some():
    with open('text.txt') as r:
        for x in r:
            yield x


# for i in some():
#     print(i.split())
p = some()
print(next(p))
print(next(p))
print(next(p))







