# Сопоставление шаблону

# str = "help me"

# match str.split():
#     case ["help"]:
#         print("HELP")
#     case ["help", "me"]:
#         print("sure")
#     case _:                                       # default
#         print("WHAT?")

# ===============================================
# Связанные переменные
# match input().split():
#     case ["help"]:
#         print("HELP")
#     case ["help", "me"]:
#         print("sure")
#     case ["help", command]:
#         print(f"The {command} is important")
#     case _:                                         # default
#         print("WHAT?")

# ===============================================

# теперь можем с command снова сделать match
# match input().split():
#     case ["help"]:
#         print("HELP")
#     case ["help", "me"]:
#         print("sure")
#     case ["help", command]:
#         print(f"The {command} is important")        # command это ровно один элемент
#         match command:
#             case "run":
#                 print("RUN")
#             case "quit":
#                 print("QUIT")
#     case ["help", *cmds]:                           # help one two -> Commands are:, '['one', 'two']'
#         print(f"Commands are:, '{cmds}'")
#     case []:
#         print("empty")
#     case _:
#         print("WHAT")

# ===============================================
# или
# match input().split():
#     case ["help" | "usage", *cmds]:
#         print("help or usage with extra parameters")
# ===============================================

# match input().split():
#     case ["help" | "usage" as hlp, *cmds]:                  # связывание с 'hlp'
#         print(hlp)
#         print(f"{hlp.upper()}: Commands are", cmds)         # HELP: Commands are ['one', 'two']
# ===============================================

#if | *_ - распаковывается ноль или больше аргументов
# match input().split():
#     case [command, *_] if len(command) == 2:
#         print("ERRR", command)
# ===============================================

# match eval(input()):
#     case float():                       # тип обьекта должен быть типа float
#         print("Float")
#     case int(x):                         # x - это связанная переменная, она должна быть типа int
#         print("Int", x)
#     case complex(real=1, imag=2):        # если у обьекта есть поля, можно перечислить поля (только с такили полями)
#         print("1+2i!")
#     case complex(real=0) as y:
#         print("Zero", y)
# ===============================================

# class C:
#     a = 1
#     b = 2
# c = C()
# match c:
#     case C(a=1):
#         print("A=1")                    # > A=1
#     case C(b=2):
#         print("B=2")
#-------------------------------------------------
# class C:
#     a = 3
#     b = 4
#     __match_args__ = "a", "b"
# c = C()
# match c:
#     case C(3,4):
#         print("3,4")                        # > 3,4
#     case C(a=1):
#         print("A=1")                    
#     case C(b=2):
#         print("B=2")

# ===============================================
# d = dict(enumerate(input().split(), 1))
# print(d)
# match d:
#     case {1: "one", 2: "two"}:
#         print("exact")
#     case {1: "one", 2: other}:
#         print("bounded", other)
#     case {2: "two", **others}:
#         print("inexact", others)

# ===============================================
# сопоставление с константой
# c = 3
# match eval(input()):
#     case c:
#         print("C =", c)
# print(c)

# 'c' перебивает нашу переменную, можно хранить переменные в namespace
class CONST:
    c = 3
match eval(input()):
    case CONST.c as res:
        print("C =", res)
# ===============================================


