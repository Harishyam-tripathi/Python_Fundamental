product = 1
num = 245

while num > 0:
    ld = num % 10
    product = product * ld
    num = num // 10

print(product)