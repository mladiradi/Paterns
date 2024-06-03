
num = int(input())

for i in range(0, num + 1):
    for ii in range(num - i):
        print(" ", end="")
    for iii in range(1, 2 * i):
        print("*", end="")
    print()
