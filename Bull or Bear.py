for i in range(int(input())):
    X,Y = map(int,input().split())
    if X>Y:
        print("LOSS")
    elif X==Y:
        print("NEUTRAL")
    else:
        print("PROFIT")