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