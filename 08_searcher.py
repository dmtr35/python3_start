import os
import time

path = os.walk('/home/dm/bin')
list = []



for addres, dirs, files in path:
    for file in files:
        full_addres = os.path.join(addres, file)
        if os.path.exists(full_addres):

            if time.time() - os.path.getmtime(full_addres) < 86400:
                list.append(full_addres)



print(list)





















