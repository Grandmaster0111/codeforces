n=int(input())
l=[]
cnt = 0
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
for i in l:
    for j in l:
        if i[0] == j[1]:
            cnt += 1
print(cnt)