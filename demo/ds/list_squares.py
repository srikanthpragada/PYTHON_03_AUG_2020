squares = []

for n in range(1, 10):
    squares.append(n * n)

print(squares)

squares = [n * n for n in range(1, 20)]
squares_even = [n * n for n in range(1, 20) if n % 2 == 0]
print(squares_even)
