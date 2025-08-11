l = list(map(int,input().split()))
cnt=0
while True:
    if l[0]>l[1]:
        break
    l[0]*=3
    l[1]*=2
    cnt+=1
print(cnt)