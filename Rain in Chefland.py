for i in range(int(input())):
    X = int(input())
    if X<3:
        print("LIGHT")
    elif X>=3 and X<7:
        print("MODERATE")
    elif X>=7:
        print("HEAVY")