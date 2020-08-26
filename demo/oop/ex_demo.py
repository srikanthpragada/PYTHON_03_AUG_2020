l = [1, 2, 4, 3]
try:
    l.remove(4)
    print("Removed!")
except KeyError:
    print("Value Error")
else:
    print("Success")
finally:
    print("Finally")

print('The End')
