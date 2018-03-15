class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


rad_man = Person("Billy Hays", "High-School")


class Employee(Person):
    def __init__(self, name, education, salary, job):
        super(Employee, self). __init__(name, education)
        self.salary = salary
        self.job = job

    def get_payed(self):
        print("You just got payed $" "%s" "beesh." % self.salary)


radder_man = Employee("Billy Ways", "High-School", "$10,000", "Mcdonalds Employee")


class Programmer(Employee):
    def __init__(self, name, education, salary, job, computer, program):
        super(Programmer, self). __init__(name, education, salary, job)
        self.computer = computer
        self.program = program

    def program(self):
        print("You just programmed a %s" % self.program)


Employee = Employee("Billy Mays", "College", "$70,000", "Yes", "iMac", "Client's Privacy")
