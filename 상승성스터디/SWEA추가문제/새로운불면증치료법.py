T = int(input()) #5
for tc in range(1,T+1):
    N = int(input()) #1
    arr = [1]*10
    k = 1
    
    while arr!=[0]*10:
        l = len(str(N*k))
        for i in range(l):
            a = int(str(N*k)[i])
            arr[a] = 0
        k += 1
        
        
    print(f'#{tc}',N*(k-1))
    