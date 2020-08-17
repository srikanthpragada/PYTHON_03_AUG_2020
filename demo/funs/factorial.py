import sys

if len(sys.argv) == 1:
    print("Please provide number on command line!")
    print("Usage : python factorial.py  number ...")
    exit(0)

num = int(sys.argv[1])
fact = 1
for i in range(1, num+1):
    fact *= i

print(f"Factorial of {num} is {fact}")