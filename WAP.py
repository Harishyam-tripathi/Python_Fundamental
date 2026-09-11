'''WAP to take a tuple as input and add all the element which are present at 
 even index number as well as odd index number sepratelly.'''

from tracemalloc import start


l = eval(input("Enter your list:"))
evensum = 0
oddsum = 0
i = 0
while i <=  len(l)-1:
    if i %2==0:
        evensum = evensum + l[i]
    else:
        oddsum = oddsum + l[i]
    i=i+1
print("Resule of addtion even number is",evensum)
print("Result of addition odd number is",oddsum)

'''WAP to take a tuple as user input and multiply those elements 
which are present at odd index number seprately.'''

l = eval(input("Enter your tuple:"))
mult =  1
i = 0
while i <= len(l)-1:
    if i%2!=0:
        mult = mult*l[i]
    i = i+1
print("Result of present odd index number is",mult)

#WAP to take a tuple as user input and multiply all the elements present in the tuple

l = eval(input("Enter your tuple:"))
mult = 1
i = 0
while i <= len(l)-1:
    mult = mult*l[i]
    i = i+1
print("Result of multiply is",mult)

#WAP to take a start and stop number from user and multiply all the odd numbers present in that range.

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
mult = 1
i = start 
while i <= stop:
    if i%2!=0:
        mult = mult*i
    i = i+1
print("Multiply of odd num is",mult)

#WAP to take a start and stop number from user and add all the odd numbers present in that range.

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
add = 0
i = start 
while i <= stop:
    if i%2!=0:
        add = add+i
    i = i+1
print("Addition of odd num is",add)

#WAP a program to add all the even starting from 1 to 100 using while loop.

sum = 0
i = 1
while i <= 100:
    if i%2==0:
        sum = sum+i
    i = i+1
print("Addition of even num is",sum)

#WAP to find the smallest digit present inside the number using while loop.

num = int(input("Enter a number: "))
smallest = 9  # Initialize smallest to the largest single-digit number
while num > 0:
    last_digit = num % 10  # Get the last digit
    if last_digit < smallest:
        smallest = last_digit  # Update smallest if current digit is smaller
    num = num // 10  # Remove the last digit
print("The smallest digit is", smallest)

