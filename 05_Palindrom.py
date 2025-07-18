n = 878
num = n
result = 0
while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

if result == n:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
