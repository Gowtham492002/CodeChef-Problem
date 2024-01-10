for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sums = 0
    
    for i in range(0, n-1):
        sums += abs(arr[i] - arr[i+1]) - 1
    
    print(sums)
