'''T = int(input()) #3
for r in range(T):
    N = int(input()) #9
    a = list(map(int, input().split())) #[7,4,2,0,0,6,0,7,0]
    li =[]
    maxV = a[0] #7
    cnt = 0
    for i in range(0,N-1): #리스트 내부에서 반복할 8번
        for j in range(i,N): # 몇 갠지 카운트를 위해 
            if maxV > a[i]:
                cnt += 1
        li.append(cnt)
    print(li)
            
    maxX = li[0]
    for k in range(N):
        if maxX < li[i]:
            maxX = li[i]

    print(f'#{r+1} {maxX}')

# 블럭이 있다고 생각하면 자신보다 오른쪽에 있는 작은 블럭의 개수를 구합니다.
N = int(input())
for test_case in range(1, N+1):
    height = int(input()) #9
    arr = list(map(int, input().split()))
    ans = [0] * height      # 리스트 미리 만들어 놓구요

    for i in range(len(arr)-1):     #맨 오른쪽 블럭은 볼 필요가 없어요
        count = 0
        for j in range(i+1, len(arr)):          # j는 i + 1부터
            if arr[i] > arr[j]:     # 자기자신과 오른쪽 비교해서 작은 거 찾으면 count++
                count += 1
        ans[i] = count      # count는 새 리스트에 넣습니다.
    # ans의 최대값 찾기
    maxV = ans[0]
    for k in range(len(ans)):       # 최대값 구하기
        if maxV < ans[k]:
            maxV = ans[k]

    print(f'#{test_case} {maxV}')
            
'''

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
    
            

    