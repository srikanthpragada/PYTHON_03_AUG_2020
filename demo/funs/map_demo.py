def extract_upper(st):
    l = []
    for c in st:
        if c.isupper():
            l.append(c)

    return ''.join(l)


names = ["Abc123", "XY", 'defg']

for n in names:
    print(len(n))

for l in map(str.upper, names):
    print(l)

for l in map(extract_upper, names):
    print(l)

print(sum(map(int, ["1", "3", "4"])))
