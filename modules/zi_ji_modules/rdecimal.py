from decimal import Decimal
def jia(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) + Decimal(str(i))
    return n
def jian(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) - Decimal(str(i))
    return n
def cheng(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) * Decimal(str(i))
    return n
def chu(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) / Decimal(str(i))
    return n
def cheng_fang(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) ** Decimal(str(i))
    return n
def kai_fang(lista):
    n = 0
    for i in lista:
        n = Decimal(str(n)) ** (1 / Decimal(str(i)))
    return n