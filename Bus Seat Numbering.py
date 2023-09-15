for i in range(int(input())):
    N = int(input())
    if  N in range(1,10+1):
        print("Lower Double")
    elif N in range(11,15+1):
        print("Lower Single")
    elif N in range(16,25+1):
        print("Upper Double")
    elif N in range(26,30+1):
        print("Upper Single")
        