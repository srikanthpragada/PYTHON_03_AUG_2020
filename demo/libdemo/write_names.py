# Take names and write them into names.txt in sorted order

names = set()
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.add(name)

with open("names.txt", "wt") as f:
    for name in sorted(names):
        f.write(name + "\n")
