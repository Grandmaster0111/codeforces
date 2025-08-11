n=int(input())
for i in range(n):
    s = input()
    ns = len(s)
    if ns>10:
        print(s[0]+str(ns-2)+s[ns-1])
    else:
        print(s)