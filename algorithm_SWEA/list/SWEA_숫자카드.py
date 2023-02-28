T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #5
    arr = list(map(int,input())) #[4,9,6,7,9]
    counts = [0] * 10
    for x in arr:
        counts[x] += 1 #[0,0,0,0,1,0,1,1,0,2]
    maxV = counts[0] #0
    for i in range(10):
        if maxV < counts[i]:
            maxV = counts[i]
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == maxV: 
        # 범위를 뒤에서부터 탐색, 카드 수가 같으면 가장 큰 수를 내야하기 때문
            print(f'#{tc} {i} {maxV}')
            break



# 갈아엎기 시룸 ㅠ
# 인덱스값 찾기 할 때 큰 값 찾는 방법 모색
'''
민석님 도움
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == maxV: 
        # 범위를 뒤에서부터 탐색, 카드 수가 같으면 가장 큰 수를 내야하기 때문
            print(f'#{tc} {i} {maxV}')
            break
'''
'''
최대값의 인덱스만 있으면 최대값은 바로 알 수 있습니다
N =5
A = [2,5,3,6,1]

maxV = A[0]
maxIdx = 0
for i in range(1,N):
    if A[maxIdx] < A[i]:
        maxIdx = i

print(maxV)
    

'''