# def decor3(f):
#     def wrapper():
#         print('Код дикоратора')
#         f()
#         print('второй код дикоратора')
#     return wrapper


# @decor3 # make = decor(make)
# def make():
#     enter = input('Enter something... ')
#     print(enter)


# print('here')
# make()

# ========================================================
def decor(f):
    def wrapper():
        print('Код дикоратора')
        try:
            h = f()
            print('второй код дикоратора')
        except Exception:
            print('вы ввели недопустимые данные')
            h = f()
        return h
    return wrapper



# def decor2(fun2):
#     def wrapper():
#         print('Код дикоратора2')
#         try:
#             fun2()
#             print('второй код дикоратора')
#         except:
#             print('вы ввели недопустимые данные')



@decor # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter

@decor
def make2():
    enter = float(input('Введите число: '))
    return enter


result = make()
result2 = make2()



print('result::', result)
print('result2::', result2)














