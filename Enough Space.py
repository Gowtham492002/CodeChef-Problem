for i in range(int(input())):
    X,Y,Z = map(int,input().split())
    if (Y+Z*2)<=X:
        print("Yes")
    else:
        print("No")