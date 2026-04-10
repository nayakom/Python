class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this Employee worked in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

om = Employee()
om.salary = 100000
om.getSalary() # Employeee.getSalary(om)
om.greet()