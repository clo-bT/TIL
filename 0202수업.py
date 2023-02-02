a = [0,4,1,3,1,2,4,1]
# 구할 때 cnt = [0] * 5 배열을 만들어서 각 숫자의 개수를 넣을거야. 
# 데이터가 0≤a≤4 라서 cnt가 5개
# 데이터에서 각 숫자의 발생 회수를 세고 정수항목으로 인덱스되는 카운트 배열에 저장
counts = [0] * 5 # cnt = [1,3,1,1,2] 
for x in a:
    counts[x] += 1

# 앞에랑 자기 자신이랑 더해서 원소 조정해 
for i in range(1,5):
    counts = counts[i - 1] + counts[i] #[1,4,5,6,8]
# 맨 뒤에서부터 보니까 1이네. 1자리로 가 [1,4,5,6,8] 에서 4자리잖아 여기서 하나 빼
# [1,3,5,6,8]에서 3자리로 가서 1을 넣어줘

def Counting_Sort(A, B, k):
    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1
    # for x in A:
    #     C(x) += 1이라고 해도 돼. 위랑 동일

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


# 순열
# {1,2,3} 을 포함하는 모든 순열
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


# 탐욕 알고리즘의 예
num = 456789
c = [0] * 12
for i in range(6):
    c[num % 10] += 1 # num % 10으로 나머지를 구하고
    num //= 10 # 1의 자리 버리기
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 1
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri ==2 : print('Baby Gin')
else : print('Lose')




