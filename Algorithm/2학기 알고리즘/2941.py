'''
ljes=njak
'''
import sys
input = sys.stdin.readline
arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
# 탐색하고 있으면 cnt += 1 탐색한 글자만큼 이동
cnt = 0
i = 0
for j in range(len(a)):
    for r in range(8):
        if i == len(a) - 1:
                break
        if a[i:i+2] == arr[r]:
            i += 2
            cnt += 1
            
        else:
            i += 1
            cnt += 1

print(cnt)

# 탐색하고 없으면 cnt += 1
