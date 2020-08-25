class A:
    def process(self):
        print(type(self))
        print('In A')


class B:
    def process(self):
        print('In B')


class C(A, B):
    def process(self):
        # Call method in both superclasses
        A.process(self)
        B.process(self)
        print("In C")

obj = A()
obj.process()

obj = C()
obj.process()
