# *
# **
# ***
# ****

n = 3
for i in range(n + 1):
    for j in range(i):
        print("* ", end="")
    print()
print()
for i in range(n):
    for j in range(i, n):
        print("* ", end="")
    print()

print()

for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)
print()

for i in range(1,n+1):
    print("  " * (n - i) + "* " * i)
print()


#triangle
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print()



#dimond
for i in range(1, n + 1,):
    print(" " * (n - i) + "* " * i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
