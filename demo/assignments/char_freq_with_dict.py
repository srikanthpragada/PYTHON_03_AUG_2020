# Character frequency
st = "How do you do"

chars = {}
for c in set(st):
    chars[c] = st.count(c)

for char, count in sorted(chars.items()):
    print(char, count)
