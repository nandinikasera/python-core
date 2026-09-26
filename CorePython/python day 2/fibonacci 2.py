num=8
i=0
a=0
b=1
print(a)
print(b)
while i<num-2:
    sum=a+b
    a=b
    b=sum
    print(sum)
    i+=1