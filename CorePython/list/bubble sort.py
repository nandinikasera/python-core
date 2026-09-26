list = [2, 5, 44, 67, 55, 3, 9, 8, 99, 0, 55]

l=len(list)
for j in range(l):
    for i in range(l-1):
        if list[i]>list[i+1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp



print(list)