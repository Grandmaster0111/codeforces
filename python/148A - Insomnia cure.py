k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
cnt = 0
s = set()
for i in [k, l, m, n]:
    s.update(range(i, d + 1, i))
print(len(s))