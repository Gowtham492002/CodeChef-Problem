for i in range(int(input())):
    X,Y = map(int,input().split())
    if X<Y*2:
        print("No")
    else:
        print("Yes")