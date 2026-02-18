myDict = {
    "fast": "in a quick manner",
    "om": "A Coader",
    "Marks": [1, 4, 3, 6, 8, 2],
    "anotherdict": {'om': 'player'},
    1: 2
}

print(type(myDict.keys())) # its shows the type of this code.
# print(list(myDict.keys())) # prints the keys of the dictionary.
# print(myDict.items()) # print the (key or value) for all items of the dictionary.

# print(myDict)
# updateDict = {
#     "friend": "friend's"
# }
# myDict.update(updateDict)
# print(myDict)


print(myDict.get("om2")) # Return's None as om2 is not present in the dictionary.
print(myDict["om2"]) # it's thows an error as om2 is not present in the dictionary.