def f(i, k, p):
    global ans

    if i == k:
        cnt = 0
        if (p[0] == p[1] == p[2]) or (p[0] + 2 == p[1] + 1 == p[2]):  # p[0]+1==p[1] and p[1]+1==p[2]
            cnt += 1
        if (p[3] == p[4] == p[5]) or (p[3] + 2 == p[4] + 1 == p[5]):
            cnt += 1
        if cnt == 2:
            return 1
        else:
            return 0
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                if f(i + 1, k,p):
                    return 1
                used[j] = 0
        return 0



T = int(input()) #3
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    A = []
    B = []
    used = [0] * 6  # 사용한 숫자인지 표시
    for i in range(6):
        A.append(arr[2*i]) #[9, 5, 5, 1, 4, 2]
        B.append(arr[2*i+1]) #[9, 6, 6, 1, 2, 1]
        a = A[:i+1]
    ans_a = f(0, 6, A)
    ans_b = f(0,6,B)
    print(ans_a,',',ans_a)