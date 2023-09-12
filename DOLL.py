for i in range(int(input())):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    for j in arr:
        if j>K:
            count += 1
    print(count)