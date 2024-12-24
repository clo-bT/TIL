'''
a = list(str(input()))
b = list(str(input()))
N, K = len(a), len(b)

#배열 생성
arr = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
answer = 0


#규칙에 따라 순차적으로 숫자를 넣어준다.
for i in range(N):
    for j in range(K):
        if a[i] == b[j]:
            arr[j+1][i+1] = arr[j][i] + 1
            answer = max(answer, arr[j+1][i+1])
        else:
            arr[j+1][i+1] = max(arr[j][i+1], arr[j+1][i])

print(answer)
'''


S1 = input()
S2 = input()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
