def factorial(num):
    mult = 1
    for i in range(1, num + 1):
        mult = mult * i
    return mult
output = factorial(7)
print("Factorial =", output)