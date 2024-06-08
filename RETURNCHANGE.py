for i in range(int(input())):
    x = int(input())
    a = ""
    if (x%10)>=5:
        a+=str((x//10)+1)
        a+="0"
        print(100-(int(a)))
    else:
        a+=str((x//10))
        a+='0'
        print(100-(int(a)))