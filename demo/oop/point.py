class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x < other.x:
            return False
        else:
            return self.y > other.y

    def __int__(self):
        return self.x * self.y


p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(1, 2)
print(p1 == p2)
print(p1)  # p1.__str__()

points = [Point(11, 22), Point(5, 6), Point(10, 20)]
for p in sorted(points):
    print(p)

print(int(p1) * 2)  # p1.__int__() *  2
