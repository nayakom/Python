level = 5

for row in range (1, level +1):
    spaces = " "*(level-row)
    stars = "*"*(2*row-1)
    print(spaces + stars)