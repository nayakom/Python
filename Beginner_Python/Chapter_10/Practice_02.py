# create a class with a class attribute a ; create an object from it and set a directly using object a = 0. Does this change the class attribute ?

# class sample:  # --> class attribute 
#     a = "Om"

# obj = sample()       # --> obj and obj.a create and set the instacne attribute
# obj.a = "Rahul"      # --> obj and obj.a create and set the instacne attribute
# # sample.a = "Rahul" # --> it can be change the class attribute.

# print(sample.a)
# print(obj.a)


# write a class train which has methods to book a ticket, get status (no. of seats) and get fare info. of train running under Indian Railways.

# class Train :
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print("**************************")
#         print(f"The name of the Train is {self.name}")
#         print(f"The seats are available in the Train are {self.seats}")
#         print("**************************")

#     def getFareInfo(self):
#         print(f"The price of the ticket is: Rs.{self.fare}")

#     def bookTicket(self):
#         if (self.seats>0):
#             print(f"Your Ticket has been booked! your seat number is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("Sorry the train is full! kindly try on tatkal")

# RajDhani = Train("RajDhani Express : 144409", 120, 5)
# RajDhani.getStatus()
# RajDhani.bookTicket()
# RajDhani.bookTicket()
# RajDhani.bookTicket()
# RajDhani.bookTicket()
# RajDhani.bookTicket()
# RajDhani.bookTicket()
# RajDhani.getStatus()
