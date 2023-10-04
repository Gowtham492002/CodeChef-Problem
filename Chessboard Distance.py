for i in range(int(input())):
    x,a,y,b = map(int,input().split())
    e = abs(x-y)
    u = abs(a-b)
    print(max(e,u))