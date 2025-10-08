nums = [5, 3, 8, 1, 1]
print(sorted(nums))                             # обичная сортировка
print(sorted(nums, reverse=True))               # сортировка в обратном порядке
# -------------------------------------------------
fruits = ['apple', 'banana', 'kiwi', 'pomegranate']
print(sorted(fruits, key=len))                  # сортировка по len(fruits[..])
# -------------------------------------------------
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
print(sorted(points, key=lambda x: x['y']))


# sorted возвращает новый результат, fruits.sort() редактирует fruits


# ====================================================================
# map 
nums = [1, 2, 3, 4]
nums2 = [4, 3, 2, 1]
print(list(map(lambda x, y: x+y, nums, nums2)))

# filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x%2, nums)))
print(list(filter(lambda x: x%2 == 0, nums)))

# ====================================================================

# сортировка object

fruits = {'apple': 4, 'banana': 3, 'kiwi': 2, 'pomegranate': 1}

print(dict(sorted(fruits.items(), key=lambda x: x[1])))                # сортировать dict по value
print(dict(sorted(fruits.items(), key=lambda x: x[1], reverse=True)))  # по value в обратнов порядке


print(dict(sorted(fruits.items(), key=lambda x: x[0])))                # сортировать по ключу
# ====================================================================






