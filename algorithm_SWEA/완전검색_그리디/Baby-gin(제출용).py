'''
def f():
    pass
T = int(input()) #3
for tc in range(1, T+1):
    arr = sorted(map(str,input()))
    ans = 'Lose'
    for i in range(4):
        if (int(arr[i]) + int(arr[i+2]))/ 2 == int(arr[i+1]):
            ans = 'Baby Gin'
            break
        if (int(arr[i]) + int(arr[i+3]))/ 2 == int(arr[i+1]) == int(arr[i+2]):
            ans = 'Baby Gin'
            break
        if arr[i] == arr[i+1] == arr[i+2]:
            ans = 'Baby Gin'
            break
    print(f'#{tc} {ans}')

'''
#교수님 풀이
def f(i, k):
    global ans
 
    if i==k:
        # print(p)
        cnt = 0
        if (p[0]==p[1]==p[2]) or (p[0]+2==p[1]+1==p[2]): # p[0]+1==p[1] and p[1]+1==p[2]
            cnt += 1
        if (p[3] == p[4] == p[5]) or (p[3] + 2 == p[4] + 1 == p[5]):
            cnt += 1
        if cnt==2:
            return 1
        else:
            return 0
    else:
        for j in range(k):
            if used[j]==0:
                used[j] = 1
                p[i] = arr[j]
                if f(i+1, k):
                    return 1
                used[j] = 0
        return 0
 
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    p = [0] * 6     # 순열
    used = [0] * 6  # 사용한 숫자인지 표시
 
    ans = f(0, 6)
    print(p)
    if ans:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
    