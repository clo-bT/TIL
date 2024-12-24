
# 패턴 매칭
# 방법 1
p ='is' # 찾을 패턴
t = 'This is a book' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t에서의 비교위치
    j = 0 # p에서의 비교위치
    while j < M and i < N: 
        # 비교할 문장이 남아 있고, 패턴을 찾기 전이면(t가 벗어나지 않도록)
        if t[i] != p[j]: # 서로 다른 글자를 만나면
            i = i - j # 비교를 시작한 위치로
            j = -1 # 패턴의 시작 전으로
        i = i + 1  # 같던 다르던 간에
        j = j + 1 # 조건에 상관없이 무조건 1 더할거야.
    if j == M: # 패턴 찾음. while문 조건 중에 j가 다 돼서 나온 거면 찾은거야
        return i - M
    else: # 검색 실패. while문 조건 중에 i가 다 돼서 나온거야.
        return -1 

# 방법 2
def bf2(p, t, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i 
        return -1
print(bf2(p,t,N,M))