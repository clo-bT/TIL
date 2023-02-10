# 백만이하 양수중 소수찾기
# 에라토스테네스의 체

N = int(input())
pnumber = [1] * (N+1)
for i in range(2, N+1):
    if pnumber[i]:
        j = 2
        while i * j <= N:
            pnumber[i*j] = 0
            j += 1
for i in range(2, N+1):
    if pnumber[i]:
        print(i, end='')