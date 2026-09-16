num =  int(input("Enter your number"))
mult = 1
while num > 0:
    ld = num%10
    mult = mult * ld
    num = num // 10
    print("Multiply all the digit num is",mult)