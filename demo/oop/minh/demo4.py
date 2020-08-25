class A:
    def process(self):
        print('In A')


class B(A):
    def process(self):
        print('In B')


class C(B, A):  # C(A,B) will throw an error
    pass


obj = C()
obj.process()
print(C.mro())
