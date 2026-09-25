def digit_sum(num):
    sum = 0
    while num > 0:
        ld = num % 10
        sum = sum + ld
        num = num // 10
    return sum
output = digit_sum(245)
print("Sum of digits =", output)