number = 153
num = number
r = 0
sum = 0

while (num > 0):
    r = num % 10
    sum = sum * 10 + r
    num = num // 10

print("the reverse is",sum)
