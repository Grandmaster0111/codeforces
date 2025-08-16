n=int(input())
for _ in range(n):
    l=list(map(int, input().split()))
    l.sort()
    if l[2]==l[1]+l[0]:
        print("YES")
    else:
        print("NO")