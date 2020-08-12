data = ["1,50", "2,60", "4,80", "3,45", "6,88", "3,60", "1,70", "4,90"]

students = {}

for d in data:
    rollno, marks = d.split(",")
    marks = int(marks)
    if rollno in students:
        students[rollno].append(marks)  # add marks to existing list
    else:
        students[rollno] = [marks]  # create a list with one element

for rollno, marks in sorted(students.items()):
    print(f"{rollno:3}  {sum(marks):4}   {marks}")
