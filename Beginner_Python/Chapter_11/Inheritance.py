# This code is based on Single Inheritance:

# class Employee:
#     company = "Google"

#     def showDetails(self):
#         print("This is an Employee")

# class Programmer(Employee):

#     language = "Python"
#     company = "YouTube"

#     def getLang(self):
#         print(f"The language is {self.Lang}")

#     def showDetails(self):
#         print("This is an Programmer. He is the best programmer in our company.")

# e = Employee()
# p = Programmer()

# e.showDetails()
# p.showDetails()
# print(p.company)


# This code is based on Multiple Inheritance:

# class Freelancer:
#     company = "Visa"
#     level = 0

#     def upgradeLevel(self):
#         self.level = self.level + 1

# class Employee:
#     company = "Friday"
#     eCode = 2

# class Programmer (Employee, Freelancer):
#     name = "Om"

# p = Programmer()
# p.upgradeLevel()
# print(p.company)


# This code is  based on Multi-level Inheritance:

class Person:
    country = "India"

    def takeBreak(self):
        print("I am breathing..")

class Employee(Person):
    company = "Google"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an Employee so I am luckly breathing..")

class Programmer(Employee):
    company = "YouTube"

    def takeBreak(self):
        print("I am an Programmer so I am breathing ++++..")

    def getSalary(self):
        print(f"No salary for Programmers..")

p = Person()
p.takeBreak()
e = Employee()
e.takeBreak()
pr = Programmer()
pr.takeBreak()