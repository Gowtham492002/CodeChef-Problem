for i in range(int(input())):
    a,b,c,x= map(int,input().split())
    if (a+b)>=x or (a+c)>=x or (c+b)>=x:
        print("Yes")
    else:
        print("No")