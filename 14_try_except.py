
# def enter():
#     number = float(input('Введите число: '))
#     print(100/number)
#     return number

# while True:
#     try:
#         number = enter()
#         print(number)

#     except ValueError:
#         print('Вы ввели не число')

#     except ZeroDivisionError:
#         print(0)
#         break

#     else:
#         print('Пользователь молодец')
#         break

#     finally:
#         print('Вывод файнели')



# ============================================================
import sys

# link = 'https://www.youtube.com, https://www.root-me.org, https://habr.com/ru/, https://translate.google.com'

url_list = [
    '/home/dm/bin/test_folder/text.txt',
    '/home/dm/bin/test_folder/text2.txt',
    '/home/dm/bin/test_folder/text25.txt',
    '/home/dm/bin/test_folder/text3.txt'
]

list_defect = []
list_info = []


# for url in url_list:
#     r = open(url, 'w')
#     r.write(link)
#     r.close()



try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            r.close()
            print('здесь')
        except Exception:
            list_defect.append(url)
            print('тут')
            sys.exit()                           # генерация ошибки
            continue
        finally:
            print(list_info)
finally:
    r = open('/home/dm/bin/test_folder/save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('Я все записал несмотря ни на что')











