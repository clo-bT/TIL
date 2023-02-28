T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = 12
 
    count = 0
    for i in range(1 << n):  # 1<<n : 부분 집합의 개수
        a = []
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                a += [arr[j]]  # j번 원소 출력
        if len(a) == N:
            sum_a = 0
            for i in range(N):
                sum_a += a[i]
            if sum_a == K:
                count += 1
 
    print(f'#{test_case}', count)