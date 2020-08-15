def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend(lst, value):
    lst.insert(0, value)


a = 10
print(id(a))
zero(a)
print(a)

# Passing mutable object
nums = [1, 2]
prepend(nums, 10)
print(nums)
