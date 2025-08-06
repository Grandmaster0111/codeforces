a=input().lower()
b=input().lower()
n=len(a)
for i in range(n):
    if a[i]>b[i]:
        print(1)
        break
    elif a[i]<b[i]:
        print(-1)
        break
    else:
        continue
else:
    print(0)