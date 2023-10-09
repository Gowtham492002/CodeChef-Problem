for i in range(int(input())):
    X,Y = map(int,input().split())
    e = X*3
    u = Y*2
    if e<u:
        print(e)
    else:
        print(u)