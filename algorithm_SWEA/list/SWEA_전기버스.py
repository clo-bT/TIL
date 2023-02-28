T = int(input()) #3
for tc in range(1, T+1):
    K,N,M = map(int,input().split()) #3,10,5
    arr = list(map(int, input().split())) #[1,3,5,7,9]
    # K 한번 충전 이동 가능 정류장
    # N 가야되는 정류장
    # M 충전기 설치된 정류장

    li = [0] * (N-1) # [1,0,1,0,1,0,1,0,1]
    for x in arr:
        li[x-1] = 1
    # 충전 몇 번 해야되는지 셀거야    
    count = 0
    i = 0
    while i <= N-K:
        if li[i+K-1] == 1:
            count += 1
            i += K
        else:
            for j in range(i+K-1, i+1, -1): # 뒤로가면서 정류장 찾아
                if li[j] == 1:
                    count += 1
                    i = j
                    print(count)
                    break
            else:
                count = 0   
        if count == 0 or i == N-K:
            break
    print(f'# {tc} {count}')

''' 
    for i in range(N-K): # K칸 앞으로 간 상태에서 정류장 찾아 0부터 7까지
        if li[i+K-1] == 1:
            count += 1
            i += K
    
        else:
            for j in range(i+K-1, i+1, -1): # 뒤로가면서 정류장 찾아
                if li[j] == 1:
                    count += 1
                    i = j
        
'''

# 교수님 풀이1
T = int(input()) #3
for tc in range(1, T+1):
    K,N,M = map(int,input().split()) #3,10,5
    arr = list(map(int, input().split())) #[1,3,5,7,9]

    busstop = [0] * (N+1)
    for x in arr:
        busstop[x] = 1
    last = 0 # 마지막 충전위치
    next = K # 충전 후 최대로 갈 수 있는 정류장 번호
    cnt = 0
    while next < N: # 종점을 도착하지 못한 때까지 반복. 종점 도착하면 끝!
        if busstop[next]: # 최대 이동위치에 충전기가 있는 경우
            last = next
            next = last + K
            cnt += 1
        else:
            tmp = 0 # 구간에서 충전기 위치
            for i in range(last+1, next):
                if busstop[i]:
                    tmp = i
                if tmp != 0: # 구간에 충전기가 있는 경우
                    last = tmp
                    next = last + K
                    cnt += 1
                else: # 구간에 충전기가 없는 경우
                    cnt = 0
                    break
    print(f'# {tc} {cnt}')  



# 교수님 풀이 2
T = int(input()) #3
for tc in range(1, T+1):
    K,N,M = map(int,input().split()) #3,10,5
    busstop = [0] + list(map(int,input().split())) + [N]
    last = 0 #마지막 충전위치
    for i in range(1,M+2):
        if busstop[i] - busstop[i-1]>K: # 통과 못하는 경우
            cnt = 0
            break
        if busstop[i] - busstop[last]>K: # 충전을 해야한다면
            last = i-1
            cnt += 1
        print(f'# {tc} {cnt}') 
