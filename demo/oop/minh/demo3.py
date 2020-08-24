class A:
    def process(self):
        print('In A')


class B(A):
    pass


class C(A):
    def process(self):
        print('In C')


class D(B, C):
    pass


obj = D()
obj.process()
print(D.mro())
