for i in range(int(input())):
    A,B,C,D = map(int,input().split())
    ingredient1 = max(A,B)
    ingredient2 = max(C,D)
    print(ingredient1+ingredient2)