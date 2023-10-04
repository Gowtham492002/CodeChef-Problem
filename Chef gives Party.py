for i in range(int(input())):
    N,X,K = map(int,input().split())
    if N*X <= K:
        print("Yes")
    else:
        print("No")