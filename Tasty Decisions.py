for i in range(int(input())):
    X,Y = map(int,input().split())
    if (X*2)>(Y*5):
        print("Chocolate")
    elif (X*2)==(Y*5):
        print("Either")
    else:
        print("Candy")