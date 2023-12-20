for i in range(int(input())):
    A,B,C = map(int,input().split())
    if B < C and B < A:
        print("Bob")
    elif (B and C > A):
        print("Draw")
    else:
        print("Alice")