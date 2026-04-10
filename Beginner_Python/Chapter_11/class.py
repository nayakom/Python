class Employee:
    company = "Omni"
    salary = 100
    location = "Mehsana"

    # def changeSalary(self, sal):
    #     self.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(50000)
print(e.salary)