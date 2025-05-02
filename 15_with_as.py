



# r = open('/home/dm/bin/test_folder/save.txt', 'a')
# r.write('something' + '\n')
# 10/0
# r.write('что-то')
# r.close()

# print('Все норм')



with open('/home/dm/bin/test_folder/save.txt', 'a') as r:
    r.write('something' + '\n')
    10/0
    r.write('что-то')



print('Все норм')























