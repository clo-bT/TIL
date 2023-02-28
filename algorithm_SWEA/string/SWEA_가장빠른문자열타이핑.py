T = int(input()) #2
for tc in range(1, T+1):
    A, B = input().split() #A="banana",B="bana"
    a = len(A)
    b = len(B)
    cnt = 0 # A 안에 B 몇?
    i = 0
    while i <= (a - b):
        if A[i:i+b] == B:
            cnt += 1
            i += b
        else:
            i += 1
        
    print(f'#{tc}', a-(cnt*b)+cnt)
    
