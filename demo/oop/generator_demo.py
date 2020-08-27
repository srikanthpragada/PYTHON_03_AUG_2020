def numbers():
    for n in range(1, 10):
        yield n


def digits(st):
    for c in st:
        if c.isdigit():
            yield c


def squares(n):
    for v in range(1, n):
        yield v * v


d = digits("Abc123Xyz")
for v in d:
    print(v)

# n = numbers()
# print(type(n))
#
# print(next(n))
# print(next(n))
