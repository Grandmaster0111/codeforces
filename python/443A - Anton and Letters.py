s=input()
ss=set()
for i in s:
    if i.isalpha():
        ss.add(i)
print(len(ss))