n=int(input())
a=['I hate ', 'I love ']
s=''
for i in range(n):
    s+=a[i%2]
    if i<n-1:
        s+='that '

print(s+'it')