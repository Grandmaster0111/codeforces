n=int(input())
s=input()
cnt=0
i=1
while i<len(s):
    if s[i]==s[i-1]:
        cnt+=1
        s=s[:i-1]+s[i:]
        i-=1
    i+=1
print(cnt)
