num = 5

for i in range(0, num):
    if not 1 <= i <= (num - 2):
        for j in range(0, num):
            print('*', end='')
            continue
        print()
    else:
        for ii in range(0, num):
            if 1 <= ii <= (num - 2):
                print(end=' ')
                continue
            print('*', end='')
        print()
