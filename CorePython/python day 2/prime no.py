num=23
a=num/2
c=0
for i in range(2,num//2):
    if num%i==0:
        c=1
        break
    else:
        c=0

if c==0:
    print("number is prime")
else:
    print("0number is not prime")