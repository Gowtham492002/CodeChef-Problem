N = int(input())
arr = list(map(int,input().split()))
even = []
odd = []
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
if len(even)>len(odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
        

    