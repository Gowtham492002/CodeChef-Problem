for i in range(int(input())):
    a,b = map(int,input().split())
    count=1
    winner=""
    while(a>=0 or b>=0):
        a=a-count
        if(a<0):
            winner="Bob"
            break
        count=count+1
        b=b-count
        if(b<0):
            winner="Limak"
            break
        count=count+1
    print(winner)
            
        
        