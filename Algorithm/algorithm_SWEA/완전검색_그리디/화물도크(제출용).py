T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #10
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append([s, e])
    arr.sort(key= lambda x : (x[1], x[0])) #종료시간 기준 정렬
    # print(arr)
    # [[1, 4], [6, 15], [6, 15], [15, 16], [2, 19], [1, 22], [14, 23], [21, 23], [12, 24], [20, 24]]
    A = [arr[0]] #[1, 4]
    f = A[0][1] #4 끝나는 시간 finish 넣어놓는 거
    for i in range(1, N):
        if f <= arr[i][0]:
            A.append(arr[i])
            f = arr[i][1]
    print(f'#{tc} {len(A)}')
'''
##교수님 코드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = []
    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))
    work.sort(key=lambda x:x[1])
 
    cnt = 1
    j = 0     # 첫 번째로 작업한 화물차
    A = [0]
    for i in range(1, N):
        if work[j][1]<=work[i][0]:  # 마지막 작업 이후에 i화물차가 작업을 시작하면
            j = i
            cnt += 1
            A.append(i)
    print(f'#{tc} {cnt}')

'''
    
'''
input
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

output
#1 4
#2 4
#3 5
'''