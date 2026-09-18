s = input("Enter a string: ")

count = 0

for i in s:
    if i.isalpha() and i not in "AEIOUaeiou":
        count = count + 1

print("Number of consonants =", count)