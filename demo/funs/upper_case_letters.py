def extract_upper(st):
    l = []
    for c in st:
        if c.isupper():
            l.append(c)

    return l
    #return ''.join(l)


print(extract_upper("How ARE You"))
