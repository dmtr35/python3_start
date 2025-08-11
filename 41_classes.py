# Наследование и исключения

# class C:
#     a = 1
# print(C.mro())                  # [<class '__main__.C'>, <class 'object'>]

# class B(C):                     # клас B унаследовал от класса C переменную a
#     e = 123

# print(C.a)                  # 1
# print(B.a)                  # 1
# print(B.e)                  # 123
# ---------------------------------------------------


# class A():
#     def __init__(self, num, num2):
#         self.value = num
#         self.value2 = num2
#     def __add__(self, other):
#         return self.__class__(self.value2 + other.value)
    
# a = A(1, 66)
# print(a.value, a.value2)
# print(a + 44)

# class B(A):
#     def __sub__(self, other):
#         return self.__class__(self.value + other.value)
    
# print()
# ---------------------------------------------------
# print((1).__add__(2))
# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):  # Определяем поведение для "+"
#         return Number(self.value + other.value)  # Возвращаем НОВЫЙ объект

# a = Number(10)
# b = Number(20)
# c = a + b  # Вызовет a.__add__(b)

# print(c.value)  # 30 (10 + 20)


# =======================================================================
# super() в множественном наследовании
# class A:
#     def __str__(self):
#         return f"<{self.val}>"                  # класс только чтобы из него брали __str__

# class B:
#     def __init__(self, val):
#         self.val = val

# class C(A, B):
#     def __init__(self, val):
#         super().__init__(f"[{val}]")

# a = A()
# b = B(250)
# c = C(123)
# # print(a.val, a)                               # 250 <__main__.B object at 0x7f18933c3b20>
# # print(b.val, b)                               # 250 <__main__.B object at 0x7f18933c3b20>
# print(c.val, c)                               # [123] <[123]>

# # является ли C потомком A
# print(issubclass(C, A))                         # является ли 'C' потомком 'A' # True
# print(issubclass(C, B))                         # является ли 'C' потомком 'B' # True
# print(issubclass(B, A))                         # является ли 'B' потомком 'A' # False

# print(isinstance(a, A))                         # является ли объект 'a' экземпляром класса 'A' или одного из его предков # True
# print(isinstance(a, C))                         # является ли объект 'a' экземпляром класса 'C' или одного из его предков # False
# print(isinstance(c, A))                         # является ли объект 'c' экземпляром класса 'A' или одного из его предков # True
# print(isinstance(c, B))                         # является ли объект 'c' экземпляром класса 'B' или одного из его предков # True

# =======================================================================

# class nstr(str):
#     def __neg__(self):
#         return self.__class__("".join(reversed(self)))

# s = nstr("hello")
# print(s)                                        # hello
# print(-s)                                       # olleh
# print(type(s))                                        # <class '__main__.nstr'>
# print(type(-s))                                       # <class '__main__.nstr'>
# print(type(s+'d'))                                    # <class 'str'>


# =======================================================================
# Исключения
# class A(Exception):
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# for cls in [A, B, C]:
#     try:
#         raise cls()                             # вызываем исключение
#     except B:
#         print("B")
#     except A:
#         print("A")
#     except C:
#         print("C")
# ---------------------------------------------------
# else
# for i in range(7):
#     try:
#         s = 12 / (i%2)
#     except ZeroDivisionError:
#         s = -1
#     else:
#         s = 2
#     print(s)
# ---------------------------------------------------
# finally
# for i in range(7):
#     try:
#         s = 12 / (i%2)
#     except ZeroDivisionError:
#         s = -1
#     finally:
#         s = i
#     print(s)
# ---------------------------------------------------
# with, дописываем __enter__, __exit__ классу чтобы он работал с with
# class W:
#     def fun(self, n):
#         return 1/n
#     def __enter__(self):
#         print("Enter")
#         return self
#     def __exit__(self, *args):
#         print(args)

# with W() as context:
#     for i in range(4, -1, -1):
#         print(context.fun(i))
# ---------------------------------------------------
# исключение s-идентификатор
# try:
#     raise SyntaxError("Message")
# except SyntaxError as E:
#     print(E, dir(E))
#     print(E.args)                                   # ('Message',)
# ---------------------------------------------------
# proxy
# from math import inf

# def divisor(a, b):
#     c = a / b
#     return -c

# def proxy(fun, *args):
#     try:
#         return fun(*args)
#     except ZeroDivisionError:
#         return inf

# for i in range(-2, 3):
#     print(i, proxy(divisor, 100, i))

# ---------------------------------------------------
# Оператор raise
# class Expectancy:
#     from random import random as __random

#     def __getitem__(self, idx):
#         if self.__random() > 6/7:
#             raise IndexError("Bad karma happens")
#         return self.__random()
# print(list(Expectancy()))
# ---------------------------------------------------
# Python3.11+: групповые исключения
# def fun():
#     raise ExceptionGroup("Oops!", [ValueError("Ping"), TypeError("Bang")])

# def catch_value():
#     try:
#         fun()
#     except* ValueError as EGroup:
#         print(EGroup.exceptions)

# try:
#     catch_value()
# except* TypeError as EGroup:
#     print(EGroup.exceptions)


