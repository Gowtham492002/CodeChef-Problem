for i in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))
    a=max(ls)
    ls1=[]
    ls2=[]
    for i in ls:
        if (i==a):
            ls1.append(i)
        else:
            ls2.append(i)
    b=max(ls2)   
    print(a+b) # NOQA
    
        
            
        