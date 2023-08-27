for i in range(int(input())):
    n, x = map(int, input().split())
    ans = str(n * x)
    if len(ans) == 5 and ans[0] != '0':
        print("Yes")
    else:
        print("No")
