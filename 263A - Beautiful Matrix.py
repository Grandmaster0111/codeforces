for i in range(5):
    s = list(map(int, input().split()))
    for j in range(5):
        if s[j]==1:
            v=[i,j]
print(abs(2-v[0])+abs(2-v[1]))
