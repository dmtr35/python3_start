class C:
    var: int
    def __init__(self, a: int) -> None:
        self.var = a
    def __str__(self) -> str:
        return(str(self.var * 2))

c = C(4)
print(c)                                # 8

c = C("QWE")
print(c)                                # QWEQWE

# указание типов не работает, если нужна строгая типизация нужно проверять в ручную