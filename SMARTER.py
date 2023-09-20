import math

for _ in range(int(input())):
    L, V, W = map(int, input().split())
    ans = math.ceil(L / V) - math.ceil(L / W) - 1
    print(ans)
