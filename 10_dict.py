# d1 = {'a': 7, 'b': 9}
# d2 = dict([[1, 2],[3, 4],[5, 6]])
# d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')

# d5 = d1.copy()                      # копируем словарь
# print(d1.items())                   # возвращает список из кортежей
# print(d1.keys())                    # возвращает ключи в словаре
# print(d1.values())                  # возвращает значение
# d1.update(d2)                       # добавляем другой словарь в конец нашего
# y = d1.get('c', 'value')            # если значения 'c' нет, вернется none вместо ошибки, или наше значение (value)
# t = d1.pop('a')                       # удаляем значение, но сохраняем его в переменную



# print(t, d1)




# ==================================================================
# print(d3)


# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}


# users = {
#     'Alex': {'pass': 452424525, 'id': 1957},
#     'Jimmy': {'pass': 4524524, 'id': 1958},
#     'Bob': {'pass': 452452425, 'id': 1959}
# }


# def buy():
#     pay = 0
#     while True:
#         enter = input('Что покупаем?\n')
#         if enter == 'end':
#             break
#         if enter not in price:
#             print('Нет такого товара!')
#             continue
#         pay += price[enter]
#     return pay

# sum = buy()
# print(sum)


# ===========================================================
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# print(my_dict['apple'])                                 # получить значение по ключу
# print(my_dict.get('apple'))                             # безопасно получить значение
# print(my_dict.get('pear', 0))

# my_dict['pear'] = 1                                       # добавить или изменить значение
my_dict['pear'] += 1                                      # добавить или изменить значение
print(my_dict)

if 'banana' in my_dict:                                   # проверить, есть ли ключ
    print('Yes!')

del my_dict['orange']                                     # удалить ключ

for k in my_dict.keys():                                  # получить список всех ключей
    print(k)

for v in my_dict.values():                                # список всех значений
    print(v)

for k, v in my_dict.items():                              # пары (ключ, значение)
    print(k, v)

print(my_dict)

my_dict.update({'grape': 4})                              # обновить словарь другим словарём, соединяет словари
print(my_dict)


x = my_dict.pop('banana')                                 # удалить ключ и вернуть значение
print(x)


print(my_dict)