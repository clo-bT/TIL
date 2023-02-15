## 부분집합
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] =i                   # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            for l in range(2):
                bit[3] = l      # 3번째 원소
                print(bit)

## powerset을 구하는 백트래킹 알고리즘
# 후보군을 추출하는 작업이 중간에 들어감
def backtrack(a,k,input):
    global Maxcandidates
    c = [0]* Maxcandidates

    if k == input:
        process_solution(a,k)           #답이면 원하는 작업을 한다
    else: 
        k += 1
        ncandidates = construct_candidates(a,k,input,c)
        for i  in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)
def construct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False
    return 2
Maxcandidates = 2
Nmax = 4
a = [0] * Nmax
backtrack(a,0,3)

# 백트래킹으로 순열 구하기



# 실습
def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1  # 1 넣고
        f(i+1, k)    # 다음 칸 이동
        bit[i] = 0
        f(i+1, k)
A = {1,2,3}
N  = len(A)
bit = [0] * N

