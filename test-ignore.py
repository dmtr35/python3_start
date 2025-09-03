# def __iter__(self):
#         return iter(self.books)

# что здесь означает слово iter, это же тоже какая то обертка?



def range(x, y, z=1):
    arr = []

    while x < y:
        arr.append(x)
        x += z
    
    print(arr)


range(1, 10, 3)