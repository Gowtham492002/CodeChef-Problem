a,b,x,y = map(int,(input().split()))
messi_points = a*2+b
ronaldo_points = x*2+y
if messi_points == ronaldo_points:
    print("Equal")
elif messi_points > ronaldo_points:
    print("Messi")
else:
    print("Ronaldo")