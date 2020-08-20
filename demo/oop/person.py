class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email  # Private attribute

    def print_details(self):
        print("Name  :", self.name)
        print("Email :", self.__email)


p = Person("Tom", 'tom@gmail.com')
#print(p.__email)
#p._Person__email = 'tommy@gmail.com'
p.print_details()
print(p.__dict__)

