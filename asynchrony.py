# def mult(name):
#     x = yield f"{name}: Give me X"
#     y = yield f"{name}: Geve me Y ({x=})"
#     return x * y
# def task(name):
#     while True:
#         value = yield from mult(name)
#         yield f"[{name}]: {value}"

# tasks = task("first"), task("second")
# next(tasks[0]), next(tasks[1])

# for i in range(20):
#     n = not i % 3
#     print(tasks[n].send(i))
# ==========================================================

# from random import randint
# def mult():
#     return (yield) * (yield)

# def task(num):
#     res = 0
#     for i in range(num):
#         res += yield from mult()
#     return res

# def loop(*tasks):
#     queue, res = list(tasks), []
#     print("Start:", *queue, sep="\n\t")
#     for task in tasks:
#         next(task)
#     while queue:
#         task = queue.pop(0)
#         try:
#             task.send(randint(3, 10))
#             print("here")
#         except StopIteration as E:
#             res.append((task, E.value))
#         else:
#             queue.append(task)
#     return res

# print("Done:", *loop(task(7), task(2), task(5)), sep="\n\t")

# ==========================================================

from random import randint
from string import ascii_uppercase
from collections import deque

def subr():
    return (yield int) * (yield str)

def task(num):
    res = ""
    for i in range(num):
        res += yield from subr()
    return res

def loop(*tasks):
    queue, result = deque((task, None) for task in tasks), []
    print("Start:", *queue, sep="\n\t")
    idx = -1
    while queue:
        task, request = queue.popleft()
        if request is int:
            data = randint(1, 4)
        elif request is str:
            data = ascii_uppercase[idx := idx + 1]
        else:
            data = request
        try:
            request = task.send(data)
        except StopIteration as ret:
            result.append((task, ret.value))
            task.close()
        else:
            queue.append((task, request))
    return result

print("Done:", *loop(task(10), task(3), task(5)), sep="\n\t")


