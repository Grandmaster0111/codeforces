n=int(input())
cnt=0
for i in range(n):
    s = input()
    if s[1]=='+':
        cnt+=1
    else:
        cnt-=1
print(cnt)
