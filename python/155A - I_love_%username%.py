n = int(input())
l = list(map(int, input().split()))
mi=l[0]
ma=l[0]
cnt=0
for i in l:
    if mi>i:
        cnt+=1
        mi=i
    if ma<i:
        cnt+=1
        ma=i
print(cnt)