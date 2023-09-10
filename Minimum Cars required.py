for i in range(int(input())):
    N = int(input())
    if N%4 == 0:
        print(N//4)
    else:
        print((N//4)+1)
    