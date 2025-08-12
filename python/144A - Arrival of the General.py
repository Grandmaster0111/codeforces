n=int(input())
a=list(map(int,input().split()))
mi=0
ma=0
for i in range(1,n):
    if a[i]<=a[mi]:
        mi=i
    if a[i]>a[ma]:
        ma=i
if mi<ma:
    print(ma+n-mi-2) 
else:
    print(ma+n-mi-1)