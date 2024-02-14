t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    for i in range(len(d)-1):
        
        if d[i] <= d[i+1]:
            continue
        else:
            print("No")
            break
        
    else:
        print("Yes")
        
    t -= 1
