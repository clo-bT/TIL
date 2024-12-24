'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnts=[0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i]+=1
    ans = max(cnts)
    print(f'#{test_case} {ans}')
'''



T = int(input())

for tc in range(1, T+1):
    cor = [0]*200
    N = int(input())
    for i in range(N):
        a, b = map(int,input().split())
        if a > b:
            a, b = b, a
        for j in range((a-1)//2, b//2):
            cor[j] += 1
    print(f'#{tc}',max(cor))
    
# 왜 틀리는지 모르겠음...