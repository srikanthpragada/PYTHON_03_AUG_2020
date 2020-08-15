g = 1


def fun1():
    global g
    g = g + 2
    a = 100

    def fun2():
        nonlocal a
        a = a + 1
        print(a)

    fun2()
    print(a)


fun1()
