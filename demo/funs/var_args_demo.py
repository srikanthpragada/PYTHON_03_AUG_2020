def wish(*names, message="Hi"):
    for n in names:
        print(message, n)


wish("Bill", "Larry", message="Hello")
wish('Mark')
