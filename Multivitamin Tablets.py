for i in range(int(input())):
    X,Y = map(int,input().split())
    if X*3 <= Y:
        print("Yes")
    else:
        print("No")