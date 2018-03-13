class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


class Employee(object):
    def __init__(self, salary, job):
        self.salary = salary
        self.job = job

    def get_payed(self):
        print("You just got payed $" "%s" "beesh." % self.salary)
        super(Employee, self). __init__(name, education)


class Programmer(object):
    def __init__(self, college_education, computer, program):
        self.college_education = college_education
        self.computer = computer
        self.program = program

    def program(self):
        print("You just programmed a %s" % self.program)
        super(Programmer, self). __init__(college_education, computer, program)