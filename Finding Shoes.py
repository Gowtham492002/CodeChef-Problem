for i in range(int(input())):
    N,M = map(int,input().split())
    if N-M<=0:
        print(N)
    else:
        print((N*2)-M)