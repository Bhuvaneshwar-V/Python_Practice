text = input('Original string is ')
print("Printing only even index chars")
for index, char in enumerate(text):
    if index %2 == 0:
        print(char)