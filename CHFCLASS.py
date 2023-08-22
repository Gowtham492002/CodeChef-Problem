for i in range(int(input())):
    N = int(input())
    if N<6:
        print("0")
    else:
        week=N//7
        rem=N%7
        if(rem==6):
            week+=1
            print(week)
        else:
            print(week)
        