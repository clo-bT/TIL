# memo를 위한 배열을 할당하고, 모두 0으로 초기화한다.
# memo[0]을 0으로 memo[1]는 1로 초기화한다.

def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0 :
        memo[n] = (fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1


# 피보나치 수 DP 적용 알고리즘
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

## 재귀 연습
# i번째 값 함수를 복사하는 재귀함수
def f(i, k):
    if i == k: #목표에 도달하면
        print(B)
        return
    else: #접근할 게 남아있으면
        B[i] = A[i] # i번째 함수를 복사해.
        f(i+1, k)

A = [10, 20, 30]
B = [0] * 3
f(0, 3)

# DFS 그래프 예시 방법
V, E = map(int, input().split())
arr = list(map(int,input().split()))
# 1. 인접행렬 하는 방법 A[i][j] = 1 or 0 간선에다 1
adjM = [[0]*(v+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1
    # 저장방법_인접 리스트 사용
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print()  


# 복사하는 함수
def f(i, k):        # i복사할 인덱스, k배열의크기
    if i == k :
        print(B)
    else:
        B[i] = A[i]
        f(i+1, k)   # 다음 인덱스를 복사하러 이동
A = [10, 20, 30]
N = len(A)
B = [0] * N
f(0,N)



# 배열 A 에 key값이 있으면 1, 없으면 0
# 재귀
def f(i,k,key):
    if i == N :             # 배열의 끝, 검색 실패
        return 0
    elif A[i] == key:       # 성공
        return 1
    else:
         f(i+1, k , key)    # 다음 원소로 이동
A = [7,2,5,3,8,9]
N = len(A)
key = 3
print(f(0,N, key)) #1
key = 6
print(f(0,N, key)) #0