step = [5,4,3,2,1]
cnt=0
n=int(input())
for i in step:
    cnt+=(n//i)
    n=n%i
print(cnt)