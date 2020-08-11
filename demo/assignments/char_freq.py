# Character frequency
st = "How do you do"

for c in sorted(set(st)):
    print(c, st.count(c))
