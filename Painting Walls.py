for i in range(int(input())):
    x,y,z=map(int,input().split())
    cost=2*x*y
    print(z//cost)