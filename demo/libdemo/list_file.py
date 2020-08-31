with open("names.txt", "r") as f:
    for (lineno, name) in enumerate(f.readlines()):
        print(f"{lineno + 1:03} : {name.strip()}", )
