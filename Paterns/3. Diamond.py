
num = int(input()) // 2

for i in range(1, num + 1):
    for ii in range(num - i + 1):
        print(" ", end="")
    for iii in range(1, 2 * i):
        print("*", end="")
    print()
for i in range(num + 1, 0, -1):
    for ii in range(num - i + 1):
        print(" ", end="")
    for iii in range(1, 2 * i):
        print("*", end="")
    print()
