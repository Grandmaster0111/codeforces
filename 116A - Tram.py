n=int(input())
m=0
cnt=0
for i in range(n):
    a,b = map(int, input().split())
    cnt-=a
    cnt+=b
    m=max(m,cnt)
print(m)