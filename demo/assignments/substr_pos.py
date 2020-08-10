ms = "How do you do"
ss = "do"

pos = 0
while True:
    pos = ms.find(ss, pos)
    if pos == - 1:
        break
    print(pos)
    pos += 1

