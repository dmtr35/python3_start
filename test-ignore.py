




class F(Exception):
    __add__ = exec

f=F()
f.__add__("__import__('os').system('ls')")
f + "__import__('os').system('ls')"


# print("F:", type(F))
# print("f:", type(f))

# try:
#     raise F
# except F as e:
#     print("e:", type(e))
#     e + "__import__('os').system('ls')"
