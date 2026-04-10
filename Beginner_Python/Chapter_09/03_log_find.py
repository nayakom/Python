# with open ("log.txt") as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is present")

# else:
#     print("No python is not present")


# finding the line on the log text.

content = True
i = 1

with open ("log.txt") as f:
    while content:
        
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i+=1