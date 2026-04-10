class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this Employee worked in {self.company} is {self.salary}")

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee Is Created !")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")
    
om = Employee("om", 1000, "YouTube")
#om = Employee() --> throws an error (missing 3 required positional arguments:)
om.getDetails()