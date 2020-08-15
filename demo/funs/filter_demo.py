st = "This 123 is FINE"


def isupper_or_digit(s):
    return s.isupper() or s.isdigit()


for c in filter(str.isupper, st):
    print(c)

for c in filter(isupper_or_digit, st):
    print(c)

for c in filter(lambda s: ord(s) > 100, st):
    print(c)

for v in filter(lambda n: n >= 50, [70, 80, 45, 34, 60]):
    print(v)

print( list(filter(lambda n: n < 50, [70, 80, 45, 34, 60])))

