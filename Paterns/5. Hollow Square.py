
n = int(input())

for i in range(1, n + 1): # Loop through rows

    for j in range(1, n + 1): # Loop to print pattern

        if (i == 1 or i == n or j == 1 or j == n): # Printing Pattern
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()




