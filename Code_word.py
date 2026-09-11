'''1- WAP to convert Celsius into forhnheit by take user_input?

C = int(input("Enter the temprature in celsius:"))
F = (1.8*C)+ 32
print("Result in forhenheit is:",F)'''

'''2-WAP to take the marks of the student who has five subject calculate the average
mark of the student.

Mark1 = float(input("Enter the marks of sub1:"))
Mark2 = float(input("Enter the marks of sub2:"))
Mark3 = float(input("Enter the marks of sub3:"))
Mark4 = float(input("Enter the marks of sub4:"))
Mark5 = float(input("Enter the marks of sub5:"))

Total = (Mark1+Mark2+Mark3+Mark4+Mark5)/5
print("Average number of student:",Total)'''

'''2-WAP to calculate the percentage of student Who has five sub.

Sub1 = int(input("Enter the num of the Hindi:"))
Sub2 = int(input("Enter the num of the English:"))
Sub3 = int(input("Enter the num of the Math:"))
Sub4 = int(input("Enter the num of the Science:"))
Sub5 = int(input("Enter the num of the SST:"))

Percent = (Sub1+Sub2+Sub3+Sub4+Sub5)/500*100
print("The percentage of the student is:",Percent)'''

'''3- WAP to convert Decimal into Binary-

num = int(input("Enter your Decimal Num:"))
print(bin(num))'''

'4- Write to convert Decimal into octal num.'

'''num = int(input("Enter your Decimal Num:"))
print(oct(num))'''

'''5- Write to convert decimal to hexa decimal.

num = int(input("Enter your Decimal Num:"))
print(hex(num))'''


'Write to add two number in python.'

'''x = 15
y = 12
res = x+y
print("Result of additon is:",res)'''

'Write to add two number in python by the user input.'
'''x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))
res = x+y
print("Result of addition is:",res)'''

'Write a program to Square a given number.'

'''num = int(input("Enter your first number:"))
res = num**2
print("Square of given num is:",res)'''

"Multiplication by the user input"

'''x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))
res =x*y
print("Result of Multiplication is:",res)'''

'Write a program to calculate the square root of a given number'

'''num = int(input("Enter your furst num:"))
res = num**0.5
print("square root of given number is:",res)'''

'Write a program to calculate area of a trangle'

'''b = float(input("Enter your first values for base:"))
h = float(input("Enter your second values for hight:"))
Area = 0.5*b*h
print("Area of trangle is:",Area)'''

'WAP to swap the value of two numbers'

'''x = int(input("Enter your first value:"))
y = int(input("Enter your second value:"))
x,y = y,x
print("value of x & y after swaping is:",x,y)'''

'Write a program to conver km to M.'

'''num = int(input("Enter your value of kilometer:"))
res = num*1000
print("The Result in meter is:",res)'''

'Wap to find the find out the smallest num among two smallest.'
'''num1 = int (input("Enter your first num"))
num2 = int (input("Enter your second num"))
if num1>num2:
    print(num1,"is smallest")
else:
    print(num2,"is smallest")'''


'wap to check weather a given char is alphabet or not.?'
'''ch = input("Enter a character:")
if ch.isalpha():
    print("It is alphabet")
else:
    print("It is not alphabet")'''

'Wap to check weather agiven alphabet is upper case or not?'
'''ch = input("Enter your character:")
if 'A'<=ch<='Z':
    print("It is Upper case")
else:
    print("It is not Upper case")'''

'If-Elif ->'

'WAP to determine the group of a person based on the given below table?'

'''Age = int(input("Enter your Age:"))
if Age>=60:
    print("This is a senior citizen")
elif Age>=20:
    print("This is an Adult person")
elif Age>=12:
    print("This is Teenage Boy")
else:
    print("This is Child")'''


'WAP to take a number 1-7 as input and print the corressponding day of the week'

'''num = int(input("Enter your number:"))

if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thrusday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("It is not number of week day")'''

'WAP to calculate the tax of a person based on the given below chat'

'''salary = int(input("Enter your salary Amount:"))
if salary>=2000000:
    print("Yor will pay 30% tax")
elif salary>=1500000:
    print("You will pay 20% tax")
elif salary>=120000:
    print("You will pay 10% tax")
else:
    print("you will pay 0 tax")'''

'''num = int (input("Enter your number:"))
if num%10==5:
    print("The last digit of num is 5")'''

'''age = int(input("Enter the age number:"))
if age>=18 and age<=60:
    print("you are Eligble")
else:
     print("Not Eligible")'''

'''ch = input("Enter your character")
if ch.isalpha() and ch.isupper():
    print("It is char and Upper case")'''

'''ch = input("Enter your character:")
if ch.isalpha() and ch in 'AEIOUaeiou':
    print("it is Vowels")'''

'''age = int(input("Enter your age number:")) 
salary = int(input("Enter your salary Amount:"))
if age>21:
    if salary>30000:
     print("you are eligible for loan")
else:
    print("You are not eligible for loan")'''

'''Exp = int(input("Enter your year of Experence:"))
salary = int(input("Enter your salary amount:"))

if Exp>=5:
    if salary>=50000:
        print("Bonus is 10000")
    else:
        print(Exp,"You are not Eligible for Bonus")
    
if Exp>=5:
    if salary>=25000:
        print(Exp,"Your Bonus is 5000")
    else:
        print("You are also not Eligible for Bonus")'''

"while loop statement"

'Wap to print your name 5 times.'

'''i=1
while i<=5:
    print("Nikhil")
    i=i+1'''

'WAP to print all the num starting from 1 to 7.'

'''i=1
while i<=7:
    print(i)
    i=i+1'''
'Wap to print all the numbers starting from 7 to 1.'

'''i=7
while i >= 1:
    print(i)
    i=i-1'''

'Wap to print all the even num starting from 1 to 10.'
'''i=1
while i <= 10:
    if i%2==0:
        print(i)
        i=i+1

 or       '''
'''i = 2
while i <= 10:
    print(i)
    i=i+2'''
'Wap to print all the odd num starting from 1 to 10:'

'''i = 1
while i <= 10:
    if i%2!=0:
        print(i)
        i=i+2'''
    
'''i = 1
while i <= 10:
    print(i)
    i=i+2'''
        
'''salary = int(input("Enter your Amouunt"))
if salary>=2000000:
    print("tax",salary*30/100)'''

#WAP to print those element only which are divisible by 5 starting from 1 to 50.

i = 1
while i <= 50:
    if i%5==0:
        print (i)
    i=i+1
           
# WAP to print all those numbers which are divisible by 3 and 5 starting from 1 to 100.
i = 1
while i <= 100:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1

 
# WAP to print all the capital letter alphabet.
i = 65
while i <= 90:
    print(chr(i))
    i=i+1

# WAP to print all the small letter alphabet.
i = 97
while i <= 122:
    print(chr(i))
    i=i+1
    
# WAP to all the capital letter alphabet in reverse order.
i = 90
while i >= 65:
    print(chr(i))
    i=i-1

# WAP all the numbers between a given arrange by the user input.
start = int(input("Enter the starting number: "))
stop = int(input("Enter the ending number: "))
i = start
while i <= stop:
    print(i)
    i=i+1


# WAP a print table of '7'.
i = 1
while i <= 10:
    print("7 *", i, "=", 7*i)
    i=i+1
    
# WAP to add the given number starting from 1 to 5.
i = 1
sum = 0
while i <= 5:
    sum = sum + i
    i=i+1
print("The sum is:", sum)

# WAP  to multiply all the given number starting from 1 to 7.
i = 1
mult = 1
while i <= 7:
    mult = mult * i
    i=i+1
    print("The multiplication is:", mult)
    
#WAP to generate infinite loop.
while True:
    print("This is infinite loop")
#or

#while 5>4:
    print("Hello world")
    

# Write to multiply all the digits present inside the given number.
# Write to add the digits that is present inside the given number.

num = int (input ("Enter your number:"))
sum = 0
while num > 0:
    last_digit = num% 10
    sum = sum + last_digit
    num = num // 10
print ("Sum of all the digit is",sum)


#Write to multiply all the digits present inside the given number.
num = int(input("Enter your number:"))
mult = 1
while num >  0:
    last_digit = num%10
    mult = mult* last_digit
    num = num // 10
print("Multiply all the digit numbers is", mult)

#WAP to find the smallest digit present inside the given numbers.
num = int(input("Enter your smallest number:"))
smallest = 9
while num > 0:
    last_digit = num % 10
    
    if last_digit < smallest:
        smallest = last_digit
    num = num // 10
print("Smallest digit =", smallest)
    
    