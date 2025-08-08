n,t = map(int, input().split())
s = list(input())
for i in range(t):
    j = 0
    while j<n-1:
        if s[j] == 'B' and s[j+1] == 'G':
            s[j]= 'G'
            s[j+1] = 'B'
            j += 1
        j += 1
print(''.join(s))