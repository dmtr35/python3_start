# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содержимое файла удаляется, если файла нет, создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет, создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'

# import os

# list_paths = []
# path = os.walk('/home/dm/bin')

# for address, dir, file in path:
#     # print('address::', address)
#     # print('dir::', dir)
#     # print('file::', file)
#     for name_file in file:
#         full_path = os.path.join(address, name_file)
#         list_paths.append(full_path)

# print(list_paths)


# r = open('/home/dm/bin/sever_path.txt', 'w')   # открываем файл для записи

# for i in list_paths:
#     r.write(i + '\n')


# r.write(text_path)                             # записываем в файл текст
# data_path = r.read()                           # читаем из файла в переменную
# print('data_path::', data_path)



# r.close                                        # закрываем файл

# ========================================================================

# r = open('/home/dm/bin/sever_path.txt')        # открываем файл для чтения

# for i in r:
#     if 'log' in i:
#         print(i)

# r.close                                        # закрываем файл

# ========================================================================

#Копируем файл и задаем скольки в эдиницу времени отводится памяти на копирование

# r = open('/home/dm/desk/Python-3.12.0.tar.xz', 'rb')    # открываем файл в 'чтение в бинарном режиме'
# y = open('/home/dm/desk/Копия_Python-3.12.0.tar.xz', 'wb')

# while True:
#     var = r.read(2362232)
#     print(var.__sizeof__())                    # сколько в оперативной памяти занимает обьект
#     if var.__sizeof__() == 33:
#         break

#     y.write(var)

# print('Контроль')
# r.close()                                      # закрываем файл
# y.close()                                      # закрываем файл

# ========================================================================
# кодировки
text = '''# z.add(6)                            # добавить в множество элемент
# z.discard(6)                        # удалить элемент (если нет, ошибки не возникает)
# z.remove(6)                         # удалить элемент (если нет, возникает ошибка)
# y = z.union(z, x)                   # обьединить множества
# z.update(x, q)                      # обьединить множества
# y = z.intersection(x)               # определить пересечения множеств(общие элементы)
# y = z.difference(x)                 # определить разницу множеств(какие в множест Z невстречаются в X)'''

r = open('/home/dm/bin/test_110.txt', 'w', encoding='UTF-8')
r.write(text)



r.close()



# h = open('/home/dm/bin/test_110.txt', 'r', encoding='UTF-16')

# result = h.read()
# print(result)

# h.close()





