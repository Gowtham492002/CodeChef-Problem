for i in range(int(input())):
    W,X,Y,Z = map(int,input().split())
    if X== W or Y== W or Z== W :
        print("Yes")
    elif X+Y == W or X+Z == W or Y+Z == W or X+Y+Z==W:
        print("Yes")
    else:
        print("No")