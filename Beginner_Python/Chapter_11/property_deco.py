class Employee:
    company = "Bharat"
    salary = 8000
    salarybonus = 2000
    # totalsalary = 1000
    
    @property
    def totalSalary(self):
        return self.salary +  self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salary =  val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 9000
print(e.salary)
print(e.salarybonus)