# class F(Exception):
#     __add__ = exec

# f=F()
# f.__add__("__import__('os').system('ls')")
# f + "__import__('os').system('ls')"


# print("F:", type(F))
# print("f:", type(f))

# try:
#     raise F
# except F as e:
#     print("e:", type(e))
#     e + "__import__('os').system('ls')"



def sec(num):
    for i in range(num):
        return i+1
    
def fun(num):
    print("first")
    arr = [100, 99, 98]
    for i in range(num):
        yield from ["a", "b", "c"]
    print("second")

print(list(fun(5)))