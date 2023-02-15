'''
N, K = map(int,input().split()) #10 4200
A = []
ans = 0
for _ in range(N):
    A.append(int(input()))
i = 1
while K != 0:
    if N == 1:
        if K % A[0] == 0:
            ans = K//A[0]
        else:
            ans = K//A[0] + 1
        break
    if K < A[i]:                   # 나눴는데 나머지가 자기 자신이면
        ans += K // A[i-1]         # 나눈 거 답에 더해놓고
        K = K % A[i-1]             #K를 갱신
        i = 0
    i += 1

print(ans)
'''
'''
N, K = map(int,input().split()) #10 4200
a = []
for _ in range(N):
    a.append(int(input()))

i = 1
ans = 0
def coin(K, arr, i):
    global ans
    if K == 0:
        print(ans)
        return
    if K % arr[i+1] == K:
        ans += K // arr[i]
        return coin(K % arr[i], arr, 0)
    else:
        return coin(K, arr, i+1)
coin(K, a, i)
'''
N, K = map(int,input().split()) #10 4200
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin #몫만큼 더하기
        K %= coin #나머지 할당
        if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
       		break
print(answer) # 거슬러 준 동전 + 화폐의 수