for i in range(int(input())):
    N = int(input())
    s = input()
    s1 = len(s)
    if s1 % 2 == 0:
        firstString = s[0:s1//2]
        secondString = s[s1//2:]
        if firstString == secondString:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

        