def fun(**params):
    print(type(params))
    print(params)


def fun2(*values, **params):
    print(values)
    print(params)


fun(a=10, b=20)
fun(n1=10, n2=20)
fun2(1, 2, 3, n1=10)
