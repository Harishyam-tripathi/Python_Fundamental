Start = int(input("Enter your number:"))
Stop = int(input("Enter your second number:"))
sum = 0
i = Start
while i <= Stop:
    if i%2!=0:
        sum = sum + i
    i = i+1
print("sum of all odd num is",sum)