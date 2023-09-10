for i in range(int(input())):
    N,X = map(int,input().split())
    people_age = list(map(int,input().split()))
    count = 0
    for j in people_age:
        if j >= X:
            count +=1
    print(count)
        