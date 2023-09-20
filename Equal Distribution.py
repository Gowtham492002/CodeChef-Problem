for i in range(int(input())):
    X,Y = map(int,input().split())
    if (X+Y) %2==0:
        print("YES")
    else:
        print("NO")