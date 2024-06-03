
num = int(input())

for i in range(num, 0, -1):
    for ii in range(i):
        print("*", end=" ")
    print()
