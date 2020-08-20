class Student:
    # class attribute (static attribute)
    totalfees = {"Python": 10000, "Java": 12000, 'DS': 20000}

    @staticmethod
    def get_total_fee(course):
       return Student.totalfees.get(course)

    # Constructor
    def __init__(self, name, course='Python', feepaid=0):
        # Object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid


    # Methods
    def payment(self, amount):
        self.feepaid += amount

    def print_details(self):
        print(self.name)
        print(self.course)
        print(self.feepaid)

    def get_due(self):
        return Student.get_total_fee(self.course) - self.feepaid


s = Student("Scott", "Python", 5000)
s.payment(3000)
s.print_details()
print('Due amount :', s.get_due())

print(Student.get_total_fee("DS"))
