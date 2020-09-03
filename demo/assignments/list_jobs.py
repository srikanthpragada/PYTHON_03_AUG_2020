from datetime import datetime

f = open("jobs.txt", "r")
ef = open("errors.txt","w")
jobs = []

for line in f.readlines():
    parts = line.split(",")
    try:
        sd = datetime.strptime(parts[0], "%d-%m-%Y")
        ed = datetime.strptime(parts[1], "%d-%m-%Y")
        title = parts[2].strip()
        period = ed - sd
        jobs.append((title, period.days))
    except:
        ef.write(line)
        pass

f.close()
ef.close()

for title, days in sorted(jobs, key=lambda t: t[1]):
    print(f"{title:30} {days:2}")
