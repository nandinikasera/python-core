num=10
sum1=0
sum2=0
a=num/2
for i in range(num):
    if(i%2==0):
        sum1=sum1+i
        #a=a+1
    else:
        sum2=sum2+i
        #b=b+1

print(sum1)
avg_even=sum1/a
avg_odd=sum2/a

print("avg of even numbers",avg_even)
print("avg of odd num is",avg_odd)