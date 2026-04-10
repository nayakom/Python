# def percent(marks):
#     p = (sum(marks)/400)*100
#     return p

# mark1 = [45, 78, 86, 77]
# percentage1 = percent(mark1)

# mark2 = [75, 98, 88, 78]
# percentage2 = percent(mark2)
# print(percentage1, percentage2)


# Default parameter

def greet(name="stranger"):
    print("Good Day, " + name)

greet("om")
greet()   # this by default took as a stranger and that is called default parameter.