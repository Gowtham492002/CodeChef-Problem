for i in range(int(input())):
    A,B,C = map(int,input().split())
    if A == max(A,B,C):
        print("Alice")
    elif B == max(A,B,C):
        print("Bob")
    else:
        print("Charlie")