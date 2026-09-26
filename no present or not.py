list = [500, 200, 100, 50, 20, 10, 5, 2, 1]
num = 50
l = len(list)

for i in range(l):
    if (list[i] == num):
        c=1

        break

    else:
        c=0

if c==1:
    print("present at",i)
else:
    print("not present")

