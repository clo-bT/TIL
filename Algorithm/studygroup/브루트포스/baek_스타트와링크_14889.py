''' N = 4 일 때만 가능

N = int(input()) #4
arr = [list(map(int,input().split())) for _ in range(N)]
# [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
s = 198
for i in range(N):
    for j in range(N):
        if i != j:
            a = arr[i][j] + arr[j][i]
            b = arr[N-1-i][N-1-j] + arr[N-1-j][N-1-i] 
            if s > abs(a-b):
                s = abs(a-b)
print(s)
'''
N = int(input()) #4
arr = [list(map(int,input().split())) for _ in range(N)]
# [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
