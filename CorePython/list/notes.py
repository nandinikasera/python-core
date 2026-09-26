list = [500, 200, 100, 50, 20, 10, 5, 2, 1]
list1 = []
num = 2526
l = len(list)

for i in range(l):
    if (num // list[i]) > 0:
        div = num // list[i]
        list1.append(div)
        num = num % list[i]
    else:
        list1.append(0))

print(list1)
