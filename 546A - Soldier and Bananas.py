k,n,w = map(int, input().split())
total_cost = (w * (w + 1) // 2) * k
if total_cost > n:
    print(total_cost - n)
else:
    print(0)
