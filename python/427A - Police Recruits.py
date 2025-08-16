n=int(input())
l=list(map(int, input().split()))
cnt=0
p=0
for i in l:
    if i==-1:
        if p>0:
            p-=1
        else:
            cnt+=1
    else:
        p+=i
print(cnt)