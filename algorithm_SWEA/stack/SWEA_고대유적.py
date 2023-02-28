'''
def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n==1:
                cnt+=1
                if mx<cnt:
                    mx=cnt
            else:
                cnt=0
    return mx
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
 
    ans = count(arr)
    t = count(arr_t)
    if ans<t:
        ans=t
    print(f'#{test_case} {ans}')
'''




T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 3
    arr = [list(map(int,input().split())) for _ in range(N)] #[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    arr_t = list(map(list,zip(*arr))) #[[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    max_arr,max_arr_t = 2,2
    for lst in arr:         # 한 줄
        cnt = 0
        for i in lst:       # 줄 안에 원소하나
            if i == 1:
                cnt += 1
                if cnt > max_arr:
                    max_arr = cnt
            else:
                cnt = 0

    for lst_t in arr_t:         # 한 줄
        cnt_t = 0
        for j in lst_t:         # 줄 안에 원소하나
            if j == 1:
                cnt_t += 1
                if cnt_t > max_arr_t:
                    max_arr_t = cnt_t
            else:
                cnt_t = 0
        
    print(f'#{tc}',max(max_arr, max_arr_t))

