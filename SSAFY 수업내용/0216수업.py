## 부분집합의 합
def f(i,k,key):
    if i == k :             # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]   # 부분집합의 합
                # print(A[j], end = ' ')
        # print(s)          # 부분집합의 합 출력
        ## 더해서 10 되는 값 찾기
        if s == key:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
        
    else:
        bit[i] = 1
        f(i+1,k,key)
        bit[i] = 0
        f(i+1,k,key)

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
bit = [0]*N
f(0,N,key)


## 부분집합의 합. 파트2
def f(i,k,s,t):     # i 원소, k 집합의크기, s i-1까지원소의합, t 목표 
    global cnt
    if s > t:       # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:    # 목표치 도달했네 남은 원소 고려할 필요 없어
        cnt += 1
        return
    elif i == k:    # 모든 원소 고려
        if s == t:
            # for j in range(k):    # 부분집합의 합의 원소가 뭐가 있는지 확인
            #     if bit[j]:
            #         print(A[j],end=' ')
            # print()
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1,k,s+A[i],t)       # A[i] 포함
        bit[i] = 0
        f(i+1,k,s,t)            # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
cnt = 0
key = 10
bit = [0]*N

f(0,N,0,key)
print(cnt)      # 합이 key인 부분집합의 수


## 순열
def f(i,k):
    if i == k:
        print(p)
    else:
        for j in range(i,k):    # i 자신하고 바꾸고 그 뒤로는 오른쪽이랑만 바꿀거야. 
                                # 왼쪽이랑 바꾸면 바꾼 거 또 바꾸는 중복 생김
            p[i], p[j] = p[j], p[i] # p[i] 결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
N = len(p)
f(0,N)



