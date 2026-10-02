A = 25
B = 48
C = 31
if A == B == C:
    print("All number are same")
elif A > B and A > C:
    print (A,"is greater than both",B ,"and", C)
elif B > C and B > A:
    print (B,"is greater than both",A ,"and", C)
else:
    print (C,"is greater than both",A ,"and", B)