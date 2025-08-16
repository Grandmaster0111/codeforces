n=int(input())
for _ in range(n):
    s=input()
    l=list(s)
    r=len(l)
    a=[]
    for i in range(r):
        if l[i]!='0':
            a.append(l[i]+'0'*(r-i-1))
    print(len(a))
    print(*a)