s=input()
l=[0,0]
for i in s:
    if i.isupper():
        l[0]+=1
    else:
        l[1]+=1
if l[0]>l[1]:
    print(s.upper())
else:
    print(s.lower())