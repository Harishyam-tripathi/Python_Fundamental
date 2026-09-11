#1. Write to print your name 5 times using while loop.
i = 1
while i <= 5:
    print("hii Harishyam")
    i = i + 1
    
#2. WAP to print all the numbers from 1-7.
i=1
while i <= 7:
    print(i)
    i = i + 1
    
#3. WAP to print all the numbers from 7-1.
i = 7
while i >= 1:
    print(i)
    i = i -1
    
#4. WAP to print all the even numbers from 1-20.
i = 1
while i <=  20:
    if i % 2 == 0:
        print(i)
    i = i+1
    
#5. WAP to print all the odd numbers from 1-20.
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i = i + 1
    
#6. WAP to print those element only which are divisible by 5 starting from 1 to 50.
i = 1 
while i <= 50:
    if i% 5==0:
        print(i)
    i = i+1

# 7. WAP to print all those element which are divisible by 3 and 5 both.
i = 1
while i <= 50:
    if i%3==0 & i%5==0:
        print(i)
    i = i+1
    
# 8. WAP to print all the capital letter in alphabets:
i = 65
while i <= 90:
    print(chr(i))
    i = i+1
    
# 9. WAP to print all the small letter in Alphabets.
i = 97
while i <=122:
    print(chr(i))
    i = i+1
    
# 10. WAP to print all the capital letter in Reverse order.
i = 90
while i >= 65:
    print(chr(i))
    i = i-1 
    
#11. WAP to print all the numbers between a given arrange.

Start = int(input("Enter your starting number:"))
Stop = int (input("Enter your stoping number:"))
i = Start 
while i <= Stop:
    print(i)
    i = i+1 
    
