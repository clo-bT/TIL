for tc in range(10):
    N = int(input()) #100
    a = list(map(int,input().split()))
    for i in range(2, N-2):
        maxV = 0
        # if문으로 조망권을 확보. 주변에서 제일 큰애 찾아 제일 큰애가 a[i]
        if a[i] > a[i-2] and a[i] > a[i+2] and a[i] > a[i-1] and a[i] > a[i+1]:
            # 두번째로 큰애 찾아서 제일 큰애에서 빼
            for j in range(-2, +3):
                if maxV > a[j] and maxV < a[i]:
                    maxV = a[j]
                    cha = a[i] - a[j]
                print(cha)

            
        # A기준으로 앞뒤합쳐서 다섯개씩 있는데 제일 크면 카운트를 올려라
       

'''
[0,0,3,5,2,4,9,0,6,4,0,6,0,0]
T = int(input()) #3
for i in range(T):
    N = int(input()) #9
    a = list(map(int, input().split())) #[7,4,2,0,0,6,0,7,0]
    li = [0] * N
    for j in range(len(a)-1):
        cnt = 0
        for k in range(j+1, len(a)):
            if a[j] > a[k]:
                cnt += 1
        li[j] =cnt
    maxX = li[0]
    for r in range(N):
        if maxX < li[r]:
            maxX = li[r]

    print(f'#{i+1} {maxX}')
    
''' 

