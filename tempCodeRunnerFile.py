num = int(input("Enter your number: "))
largest = 0
smallest = 9

while num > 0:
    ld = num % 10

    if ld > largest:
        largest = ld

    if ld < smallest:
        smallest = ld

    num = num // 10

print("Maximum digit is", largest)
print("Minimum digit is", smallest)