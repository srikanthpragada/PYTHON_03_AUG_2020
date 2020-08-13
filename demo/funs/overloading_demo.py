def add(n1, n2):
    return n1 + n2


add2 = add


def add(n1, n2, n3):
    return n1 + n2 + n3


print(add2(10, 20))
print(add(10, 20, 30))
