import asyncio
# асинхронность с помощью yield
# 
# # def mult(name):
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

# from random import randint
# from string import ascii_uppercase
# from collections import deque 

# def subr():
#     return (yield int) * (yield str)

# def task(num):
#     res = ""
#     for i in range(num):
#         res += yield from subr()
#     return res

# def loop(*tasks):
#     queue, result = deque((task, None) for task in tasks), []
#     print("Start:", *queue, sep="\n\t")
#     idx = -1
#     while queue:
#         task, request = queue.popleft()
#         if request is int:
#             data = randint(1, 4)
#         elif request is str:
#             data = ascii_uppercase[idx := idx + 1]
#         else:
#             data = request
#         try:
#             request = task.send(data)
#         except StopIteration as ret:
#             result.append((task, ret.value))
#             task.close()
#         else:
#             queue.append((task, request))
#     return result

# print("Done:", *loop(task(10), task(3), task(5)), sep="\n\t")
# =========================================================================================
# =========================================================================================


# asynchrony

# from random import randint
# from string import ascii_uppercase
# from collections import deque
# from asyncio import coroutine

# @coroutine
# def subr():
#     return (yield int) * (yield str)

# async def task(num):
#     res = ""
#     for i in range(num):
#         res += await subr()
#     return res

# def loop(*tasks):
#     queue, result = deque((task, None) for task in tasks), []
#     print("Start:", *queue, sep="\n\t")
#     idx = -1
#     while queue:
#         task, request = queue.popleft()
#         if request is int:
#             data = randint(1, 4)
#         elif request is str:
#             data = ascii_uppercase[idx := idx + 1]
#         else:
#             data = request
#         try:
#             request = task.send(data)
#         except StopIteration as ret:
#             result.append((task, ret.value))
#             task.close()
#         else:
#             queue.append((task, request))
#     return result

# print("Done:", *loop(task(10), task(3), task(5)), sep="\n\t")

# =========================================================================================
# from time import strftime

# async def late(delay, msg):
#     await asyncio.sleep(delay)
#     print(msg)

# async def main():
#     print(f"> {strftime('%X')}")
#     await late(1, "One")
#     print(f"> {strftime('%X')} + 1")
#     await late(2, "Two")
#     print(f"> {strftime('%X')} + 2")

# asyncio.run(main())
# =========================================================================================
# from time import strftime

# async def late(delay, msg):
#     await asyncio.sleep(delay)
#     print(msg)

# async def main():
#     task1 = asyncio.create_task(late(2, "Two"))
#     task2 = asyncio.create_task(late(3, "Three"))
#     await task1
#     print(f"> {strftime('%X')} + 3")
#     await task2
#     print(f"> {strftime('%X')} + <<1>>")

# asyncio.run(main())
# =========================================================================================

# import asyncio

# async def late(delay, msg):
#     await asyncio.sleep(delay)
#     print(msg)
#     return delay

# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(late(3, "A"))
#         tg.create_task(late(1, "B"))
#         tg.create_task(late(2, "C"))
#     print("Done")

# asyncio.run(main())
# =========================================================================================
# TCP сервер (аналог netcat -l)

async def echo(reader, writer):
    while data := await reader.readline():
        writer.write(data.swapcase())
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(echo, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())









