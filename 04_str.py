# методы строк

s = 'stroka texta'
# bool = 1
print('str' in s)                                                 # поиск по строке (True/False)

#  ======== Проверка начала и конца строки: ========
# bool = s[1:4] == "tro"                                            # сравнение на первые, второй, третий символ
# bool = s.startswith("str")                                        # проверяет, начинается ли строка с prefix
# bool = s.endswith("xta")                                          # проверяет, заканчивается ли строка на suffix
# s = "hello world".removeprefix("hel")                             # обрезает первые три символа, возвращает остачу строки
# s = "hello world".removesuffix("rld")                             # обрезает посленние три символа, возвращает остачу строки

# ======== Поиск в строке: ========
# bool = "hello".find("e")                                          # ищет sub, возвращает индекс (или -1 если нет).   
# bool = "hello".index("e")                                         # как find, но если нет — ошибка.  
# count = s.count("str")                                            # количество повторений подстроки "str" в строке s
# count = s.count("str", 0, 10)                                     # количество повторений подстроки "str" в строке s в диапазоне start - end

# ======== Проверки типа содержимого: ========
# bool = "abc123".isalnum()                                         # только буквы и цифры.
# bool = "abc".isalpha()                                            # только буквы.
# bool = "abc".isalpha()                                            # только цифры (для десятичных чисел)
# bool = "variable1".isidentifier()                                 # можно ли использовать как имя переменной.
# bool = hello".islower()                                           # все буквы маленькие
# bool = "123".isnumeric()                                          # только цифры (включая, например, дроби в других языках).
# bool = "hello world!".isprintable()                               # все символы печатные.
# bool = "   \n\t".isspace()                                        # только пробельные символы.
# bool = "Hello World".istitle()                                    # первая буква каждого слова большая.
# bool = "HELLO".isupper()                                          # все буквы большие.

# ======== Выравнивание текста: ========
# s = "hi".center(6)                                                # центрирует текст, добавляет пробелы.
# s = "hi".rjust(5)                                                 # выравнивает вправо
# s = "hi".ljust(5)                                                 # выравнивает влево.

# ======== Изменение регистра: ========
# s = "HELLO".lower()                                               # сделать все буквы маленькими.
# s = "hello".upper()                                               # сделать все буквы маленькими.
# s = "HeLLo".swapcase()                                            # поменять регистр на противоположный.
# s = "hello world".title()                                         # каждое слово с большой буквы.
# s = "hello world".capitalize()                                    # только первая буква строки большая.

# ======== Работа с заменой текста: ========
# s = "hello world".replace("world", "python")                      # заменить одно на другое.
# s = "hello\tworld".expandtabs(4)                                  # заменить табы (\t) на 4 пробела.
# s = "hello world".replace("world", "python")                      # заменить одно на другое.


# s = "  hello  ".strip()                                           # убрать пробелы с начала и конца.
# s = "...hello...".strip(".")                                      # убрать все символы с начала и конца.
# s = "...hello world...".rstrip('.')                               # удалить все символы справа от строки
# s = "...hello world...".lstrip('.')                               # удалить все символы слева от строки

# ======== Поиск справа: ========
# bool = "banana".rfind("a")                                        # ищет с конца, возвращает индекс (или -1)
# bool = "banana".rindex("a")                                       # как rfind, но если нет — ошибка.
# s = "hello world".rpartition(" ")                                 # разделить строку на 3 части по последнему sep → 'hello', ' ', 'world'

# ======== Разделение строк: ========
# s = "one two three".rsplit(" ", 1)                                # разделить строку справа налево. → ['one two', 'three']
# new_path = "C:/Users/PyHS/Desktop/s.py".replace('/', '\\')        # заменить подстроку
# new_path = "C:/Users/PyHS/Desktop/s.py".replace('/', '\\', 1)     # заменить только первую подстроку
# new_path = "C:/Users/PyHS/Desktop/s.py".split('/')                # разбиваем по разделителю '\'

# ======== дополнительные методы: ========
# s = "a b c".split()                                               # без параметров просто разбивает строку на список  → ['a', 'b', 'c']
# s = "hello &world...".split("&")[0]                               # удалить все после символа &
# new_path = "C:/Users/PyHS/Desktop/s.py".split('/')                # разбиваем по разделителю '\'

# s = "Hello {}".format("World")                                    # Форматировать строку    → 'Hello World'
# s = "{1},,, {1},,,{0}".format(123, 456)                             # → 456,,, 456,,,123

s = " ".join(["a", "b", "c"])                                     # Соединить список строк через сепаратор   → 'a b c' 
s = "|".join(["a", "b", "c"])                                     # Соединить список строк через сепаратор   → 'a|b|c' 


# ======== строка закодирована в байты: ========
# encoded_text = s.encode('ascii', errors='ignore')                 # строка закодирована в байты (errors='replace - Ошибочные символы заменяются знаком вопроса ?)
# print(encoded_text)

# print(bool)
# print(count)
# print(new_path)
# print(s)





# ============================================================

# r = open('/home/dm/bin/test_110.txt')
# text = r.read()
# text = text.replace('\"', '')
# text = text.replace('(', '')
# text = text.replace(')', '')
# text = text.replace('\n', '\t')


# print(text)
# r.close()

# ============================================================
# enter = input('Your name: ')
# python = 'Python'


# print('Hello %s, I am %s' % (enter, python))
# print(f'Hello {enter}, I am {python}')
# a, b, c = 123, "EWT", 1.23
# print(f"{a+1} --- {c:10} text {b[:2]}")                         # → 124 ---       1.23 text EW ({a+1} - посчитало число; {c:10} вывод с шириной 10; {b[:2]} обрезать строку)

# n = 5
# a = 12
# print(f"{a:{n}}")                                               # → '   12'

# n = 2
# a = 122
# print(f"{a:{n}b}")                                              # → 1111010 (перевод с бирнарный)
# ============================================================


# print(ord("\n"))                                                  # номер спецсимвола  # → 10
# print(ord("a"))                                                   # номер спецсимвола  # → 97







