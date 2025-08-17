k,r = map(int,input().split())
cnt=1
while True:
    if k*cnt % 10 == r or k*cnt % 10 == 0:
        print(cnt)
        break
    cnt += 1