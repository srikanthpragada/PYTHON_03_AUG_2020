# Display dept wise total salary

depts = {}

with open("employees.txt", "rt") as f:
    for line in f.readlines():
        line = line.strip()   # trim new line at the end
        parts = line.split(",")
        # Ignore lines that do no have 3 elements
        if len(parts) < 3:
            continue

        name = parts[2]
        salary = int(parts[1])
        if name in depts:
            depts[name] = depts[name] +  salary   # add salary to existing total
        else:
            depts[name] = salary  # insert new entry with deptname and salary


for name, total in depts.items():
    print(f"{name:10}  {total:10}")




