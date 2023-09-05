for i in range(int(input())):
    x,y = map(int,input().split())
    if (x-100)>(y*2-200):
        print("FIRST")
    elif (x-100)==(y*2-200):
        print("BOTH")
    else:
        print("SECOND")