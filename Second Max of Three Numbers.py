for i in range(int(input())):
    N = list(map(int,input().split()))
    N.remove(max(N))
    print(max(N))