import globals_2

y = 20

def show(x):
    a = 66
    # print("b.globals:", globals().keys())
    # print("b.globals:", globals()['globals_2'].x)
    print("loc:", locals().keys())
    print("dir:", dir(a))

print("loc_here:", locals().keys())
print("dir_here:", dir())

globals_2.show()
show(33)

