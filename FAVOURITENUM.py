for i in range(int(input())):
    A = int(input())
    if A%2==0 and A%7==0:
        print("Alice")
    elif A%2!=0 and A%9==0:
        print("Bob")
    else:
        print("Charlie")