# Positional-only arguments
def fun(n1, n2, /):
    print(n1, n2)


fun(10, 20)
fun(10, 30)
