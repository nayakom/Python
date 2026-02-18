# num = int(input("Enter a number: "))
# prime = True

# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break

# if prime:
#     print("This number is prime.")
# else:
#     print("This number is not prime.")


# Write a program and print star's pattern
#     *
#   * * *
# * * * * *

#& 

#     *
#    * * 
#   * * *
#  * * * *
# * * * * * 

# n = 5

# for i in range(5):
#     print(" " * (n-i-1), end="")
#     print(" " * (n-i-1), end="")
#     print("*" * (3*i+1), end="")
#     print(" " * (n-i-1), end="")
#     print(" " * (n-i-1))

# write a python program in multiplication in rever

num = int(input("Enter a number: "))
for i in range(11, 1):
    print(f"{num} X {i} = {num * i}")