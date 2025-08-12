n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
s = set()
for i in range(1,len(p)):
    s.add(p[i])
for i in range(1,len(q)):
    s.add(q[i])

if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")