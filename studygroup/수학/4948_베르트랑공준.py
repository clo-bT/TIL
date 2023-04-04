import sys
input = sys.stdin.readline
ans = 0
while True:
    N = int(input())
    if N == 0:
        print(ans)
        break
    else:
        ans = 0
        arr = []
        for i in range(N, 2*N+1):
            arr.append(i)
        # print(arr)
        for i in arr:
            cnt = 0
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        cnt += 1
                if cnt == 0:
                    ans += 1
        print(ans)