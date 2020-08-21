class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_details(self):
        print("Name    : ", self.name)
        print("Salary  : ", self.salary)


class Programmer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang

    def print_details(self):
        super().print_details()
        print("Lang    : ", self.lang)



p = Programmer("Steve",90000,"Python")
p.print_details()

