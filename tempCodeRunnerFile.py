num = int(input("Enter your number:"))
rev = 0
while num > 0:
    ld = num % 10
    rev = 10*rev + ld
    num = num// 10
print("Reverse of a number is",rev)
