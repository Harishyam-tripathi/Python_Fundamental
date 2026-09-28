#what is Function..?
#Function is a named block of code which is used to perform a specific task..

#Write to add two number using function.

def addition():
    num1 = int(input("Enter your first nummber:"))
    num2 = int(input("Enter your second number:"))
    res = num1+ num2
    print("Result of addition is",res)
addition()
print("Hello_World")
addition()

#or

def addition(a,b):
    res = a + b
    print("Result of addition is",res)
addition(50,40)

#Write to multiply two number by taking user input as argument.

def multiply():
    
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your secondd nummber:"))
    res = num1*num2
    print("Result of multiply is",res)
multiply()

#Write to print factorial number of a given number:

def fact():
    num = int(input("Enter your number:"))
    mult =1
    for i in range (1,num+1):
        mult = mult*i
    print("Factorial of a given is", mult)
fact()

#or

def fact(num):
    mult = 1
    for i in range (1,num+1):
        mult = mult*i
        print("Factorial of a given num is",mult)
fact(5)
fact(9)


def fibonacci():
    length = int(input("Enter your length of fibonacci:"))
    n1,n2 = 0,1
    print(n1,n2,end = " ")
    for i in range (length -2):
        next = n1 + n2
        print(next, end=" ")
        n1 = n2
        n2 = next
fibonacci()
print()
fibonacci()


a = 5
b = 10
res =a*b
print("Result of the multiply is",res)


#Return function
def add (n1,n2):
    res = n1+n2
    return res
output = add(2,7)
print("Result of addition is",output)
print("Result of square is",output**2)

def sample():
    print("Hello world")
    print("We love to code")
    return
    print("Bye bye")
sample()

def add (n1,n2):
    res = n1+n2
    return res,n1,n2
output, num1,num2 = add(2,7)
print("Result of addition is", output)
print("Result of num is used for the addition is",num1,num2)

def add (n1,n2):
    res = n1+n2
    return res, n1,n2
output= add(2,5)
print("Result of addition is",output[0])
print("Num used in addition is",output[1],output[2])

#type of variable in function:
#1. Global Variable- It is created outside the function body.
#2. Local Variable- It is created inside the function body.


x = 10
print("Vlue of x is",x)
def sample():
    print("Value of x is",x)
sample()


#Check even or odd

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
output = check(6)
print("Number is", output)

#Find factorial

def factorial(num):
    mult = 1
    for i in range(1, num + 1):
        mult = mult * i
    return mult
output = factorial(7)
print("Factorial =", output)

#Find largest of two numbers
def largest(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
output = largest(25, 40)
print("Largest number =", output)

#Find sum of digits
def digit_sum(num):
    sum = 0
    while num > 0:
        ld = num % 10
        sum = sum + ld
        num = num // 10
    return sum
output = digit_sum(245)
print("Sum of digits =", output)

