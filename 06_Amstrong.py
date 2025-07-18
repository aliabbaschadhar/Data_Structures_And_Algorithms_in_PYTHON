from math import pow, log10

n = 1634
num = n
count = int(log10(n) + 1)
result = 0
while num > 0:
    last_digit = num % 10
    result += pow(last_digit, count)
    num = num // 10

if result == n:
    print("Num is armstrong")
else:
    print("Num is not armstrong")
