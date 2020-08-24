class A:
    def processing(self):
        print('In A')


class B:
    def process(self):
        print('In B')


class C(A, B):
    pass
    # def process(self):
    #     print('In C')


obj = C()
obj.process()
