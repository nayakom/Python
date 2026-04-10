# A spam comment is definded as a text contaning following keywords:
#make a lot of money, "buy now", "subscribe this", "click this". write a program to detect these spams.

# text = input("Enter the text\n")

# if("make a lot of money" in text):
#     spam = True

# elif("buy now" in text):
#     spam = True

# elif("click this" in text):
#     spam = True

# elif("subscribe this" in text):
#     spam = True

# else :
#     spam = False

# if(spam):
#     print("this text is spam")

# else:
#     print("this text is not a spam")


# write a program which finds wheather a given username contains less than 10 characters or not:

# def check_username(username):
#     return len(username) > 10

# user_input = input("Enter a username to check: ")

# is_short = check_username(user_input)

# if is_short:
#     print(f"'{user_input}' contains less than 10 characters.")
# else:
#     print(f"'{user_input}' contains 10 or more characters.")


# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 -> ex, 80-90 -> A, 70-80 -> B, 60-70 -> C, 50-60 -> D, <50 -> F


marks = int(input("Enter your marks: "))

if marks>=90:
    grade = "Ex"

elif marks>=80:
    grade = "A"

elif marks>=70:
    grade = "B"

elif marks>=60:
    grade = "C"

elif marks>=50:
    grade = "D"

else:
    grade = "F"

print("Your grade is " + grade)