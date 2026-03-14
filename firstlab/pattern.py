import string

letters = string.ascii_uppercase

for i in range(1, 6):
    for j in range(i):
        print(letters[j], end=" ")
    print()