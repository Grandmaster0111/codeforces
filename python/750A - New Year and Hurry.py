n,k = map(int, input().split())
k=240-k
cnt=0
for i in range(1,n+1):
    if k>=i*5:
        k-=i*5
        cnt+=1
    else:
        break
print(cnt)
