# Program to display average of given positive numbers

total = 0
count = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break    # Terminate loop

    if num < 0:
        continue

    total += num
    count += 1

print("Average = ", total / count)