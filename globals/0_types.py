import types

# создаем модуль вручную
my_module = types.ModuleType('my_module')
my_module.x = 42
print(my_module.x)  # 42

# создаем класс вручную
MyClass = type('MyClass', (), {'x': 42})
obj = MyClass()
print(obj.x)  # 42
