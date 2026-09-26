number = 1551
num = number
r = 0
sum = 0

while (num > 0):
    r = num % 10
    sum = sum * 10 + r
    num = num // 10

if number==sum:
    print("number is palindrome")
else:
    print("number is not palindrome")