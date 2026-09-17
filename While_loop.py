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
    
#12. Write a program to print the table of '7'.

i = 1 
while i <= 10:
    print ("7*",i,"=",7*i)
    i= i+1

# 13. WAP to print the table of '12'.

i = 1 
while i <= 10:
    print ("12 *" ,i,"=", 12*i)
    i = i+ 1

# 14.WAP add all the given num is starting from 1 to 5.

i = 1
sum = 0
while i <= 5:
    sum = sum +  i
    i = i+1
print("Addition all the number is",sum)

# 15.WAP add all the given num is starting from 1 to 15.

i = 1
sum = 0
while i <= 15:
    sum = sum +i
    i = i + 1
print("addition Result is",sum)

#16. WAP to multiply all the given num is starting from 1 to 7.

i = 1
mult =1 
while i <= 7:
    mult = mult * i
    i = i + 1
print ("Result of multiply is",mult)

# Generate Infinite loop.

while 5>4:
    print("it is infinite loop")
    
#16. WAP to count the number of digit 457 inside the given number.
 

count = 0
num = 457
while num > 0:
    count = count + 1
    num = num//10
print("Number of digit present inside the given num is:",count)
    

#17. WAP to count the number of digit 457 inside the given number by user input.

num= int(input("Enter your number:"))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
  
print("Number of digit present inside the given num is",count)



# 18. WAP to add all the digit that is preset inside the given number.

sum = 0
num = 245
while num > 0:
    ld = num % 10
    sum = sum + ld
    num = num // 10
print(sum)
    
# 18. WAP to add all the digit that is preset inside the given number by user input. 
   
num = int (input("Enter your number:"))
sum = 0
while num > 0:
    ld = num % 10
    sum = sum + ld
    num = num // 10
print(sum)

# 19.WAP to multiply all the digit present inside the given number.
num = int(input("Enter a number: "))

product = 1

while num > 0:
    digit = num % 10
    product = product * digit
    num = num // 10

print("Product of all digits =", product)


#20.WAP to multiply all the digit present inside the given number.

num =  int(input("Enter your number"))
mult = 1
while num > 0:
    ld = num%10
    mult = mult * ld
    num = num // 10
    print("Multiply all the digit num is",mult)
    
##21.WAP to multiply all the digit present inside the given number.  
    
product = 1
num = 245

while num > 0:
    ld = num % 10
    product = product * ld
    num = num // 10

print(product)


# 22.WAP to find out the largest digit of a given number.

num = int (input("Enter your num:"))
largest = 0
while num > 0:
    ld = num %10
    if ld > largest:
        largest = ld
    num = num // 10
print("Largest number is",largest)

# 23.WAP to find out the smallest digit present inside the given number.

num = int (input("Enter your number:"))
smallest = 9
while num > 0:
    ld = num % 10
    if ld < smallest:
        smallest = ld
    num = num // 10
print("Smallest digit numbers is",smallest)



Start = int(input("Enter your number:"))
Stop = int(input("Enter your second number:"))
i = Start
while i <= Stop:
    if i%2==0:
        print(i)
    i = i+1

#WAP a program to add the even number starting from 1 to 100.
sum = 0
i = 1 
while i <= 100:
    if i % 2==0:
        sum = sum + i
    i = i+1
print("sum of all the given even number is",sum)


#WAP a program to add the odd number starting from 1 to 100.

sum = 0
i = 1 
while i <= 10:
    if i % 2!=0:
        sum = sum + i
    i = i+1
print("sum of all the given odd number is",sum)


