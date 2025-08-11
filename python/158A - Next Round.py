n,k = map(int, input().split())
a = list(map(int, input().split()))
cnt=0
for i in a:
    if i>=a[k-1] and i>0:
        cnt+=1
print(cnt)