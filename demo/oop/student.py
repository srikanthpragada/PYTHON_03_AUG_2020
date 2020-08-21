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

    @property
    def coursename(self):
        return self.course.upper()

    @coursename.setter
    def coursename(self, newvalue):
        if newvalue in Student.totalfees:
            self.course = newvalue
        else:
            raise ValueError("Invalid course name")

    # Methods
    def payment(self, amount):
        self.feepaid += amount

    def print_details(self):
        print(self.name)
        print(self.course)
        print(self.feepaid)

    @property
    def due_amount(self):
        return Student.get_total_fee(self.course) - self.feepaid

    @property
    def totalfee(self):
        return Student.get_total_fee(self.course)

    def __str__(self):
        return f"{self.name} - {self.course} - {self.totalfee} - {self.feepaid}"


s = Student("Scott", "Python", 5000)
print(s)
s.coursename = "Java"
print(s.coursename)

s.payment(3000)
s.print_details()
print('Due amount :', s.due_amount)
print(Student.get_total_fee("DS"))
