import globals_2

y = 20

def show():
    print("b.globals:", globals().keys())
    print("b.globals:", globals()['globals_2'].x)

globals_2.show()
show()


