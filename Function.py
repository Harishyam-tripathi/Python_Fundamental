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