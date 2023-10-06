for i in range(int(input())):
    X,Y,A,B = map(int,input().split())
    e = abs(X+Y)
    f = abs(A+B)
    print(min(e,f))
    