nums = [10, -10, 30, 40, -2]

for n in sorted(nums, key=abs):
    print(n)

names = ["c","abc","xy","de","pqrs"]
for s in sorted(names):
    print(s)

for s in sorted(names, key=len):
    print(s)
