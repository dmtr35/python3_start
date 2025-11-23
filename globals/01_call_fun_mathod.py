# How many ways are there to call a function/method other than lmao()/lm.oa()?

def f(arg):
    print(f"function <f>, arg: {arg}")

class F:
    def f(self, arg):
        print(f"method <f>, arg:{arg}")

f_obj = F()

# 1. Direct call syntax (normal way)
f(42)
f_obj.f(42)

# 2. Using getattr + call
# getattr(obj, name, default) — это встроенная функция Python.
getattr(f_obj, "f")                                         # возвращает ссылку на метод
getattr(f_obj, "f")(43)                                     # скобки делают вызов


# 3. Via __call__ magic method
f.__call__(44)
f_obj.f.__call__(44)

# 4. Вызов метода напрямую через класс
F.f(f_obj, 45)

# 5. Использовать globals() / locals()
globals()['f_obj'].f(46)
globals()['f'](46)
globals()['f'].__call__(46)
locals()['f_obj'].f(46)
locals()['f'](46)

# 6. Через eval и exec
eval("f(47)")
exec("f(47)")
eval("f_obj.f(47)")
exec("f_obj.f(47)")

# 7. Через __import__
# Достаём функцию из текущего модуля
__import__("__main__").f(48)
__import__("__main__").f_obj.f(48)

# 8. Через operator хелперы
# Модуль operator даёт удобные фабрики для вызова:
__import__("operator").methodcaller('f', 49)(f_obj)

# 9. Через functools.partial
# Создаём обёртку, которая уже знает аргументы:
__import__("functools").partial(f, 50)()
# >>> __import__("functools").partial(f_obj.f, 50)
# functools.partial(<bound method F.f of <__main__.F object at 0x7f2e0fc226c0>>, 50)

# 10. Через types.FunctionType
# Функцию можно «создать заново» из её кода и вызвать:
__import__('types').FunctionType(f.__code__, globals())(51)

# 11. Через bound/unbound метод
# Ты можешь сохранить ссылку и потом вызывать её:
meth = f_obj.f
meth(52)

# 12. __getattribute__
# То, что делает getattr, можно вызвать напрямую через магию:
f_obj.__getattribute__('f')(53)

# 14. inspect.getattr_static
# inspect умеет доставать атрибуты без магии привязки. Иногда полезно:
__import__("inspect").getattr_static(f_obj, 'f')(f_obj, 55)

# 15. operator.attrgetter
# через attrgetter:
__import__('operator').attrgetter('f')(f_obj)(56)

# 16. Через __dict__
# Функции и методы можно достать напрямую из словаря объекта или класса:
F.__dict__['f'](f_obj, 57)

# 17. Через map
# map может «прогнать» функцию по итерируемому:
list(map(f, [59]))

# 18. Через lambda-обёртку
# Функцию можно обернуть и вызвать косвенно:
(lambda g: g(60))(f)

# 19. Через setattr + getattr
# Можно временно повесить функцию на объект и вызвать её:
setattr(f_obj, 'temp', f)
getattr(f_obj, 'temp')(61)

# 20. Через __builtins__
# Функции можно вытаскивать и из пространства имён встроенных:
__import__("builtins").eval("f(62)")




