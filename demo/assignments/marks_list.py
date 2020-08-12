data = ["1,50", "2,60", "4,80", "3,45", "6,88", "3,60","9-90"]

students = {}

for d in data:
    parts = d.split(",")
    if len(parts) != 2:
        continue

    rollno, marks = parts
    students[rollno] = marks

for rollno, marks in sorted(students.items()):
    print(f"{rollno} - {marks}")
