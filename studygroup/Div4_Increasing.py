t = int(input()) #테스트케이스스
for tc in range(1, t+1):
    n = int(input()) #행렬의길이
    a = list(map(int,input().split())) #행렬의원소
    b = set(a)
    if len(a) == 1:
        print('Yes')
    else:
        if len(b) == len(a) :
            print('Yes')
        else:
            print('No')
    