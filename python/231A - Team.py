n = int(input())
cnt = 0
for i in range(n):
    m = map(int, input().split())
    if(sum(m)>1):
        cnt+=1
print(cnt)