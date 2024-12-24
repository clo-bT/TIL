import sys
input = sys.stdin.readline
arr = []
for _ in range(5):
    a = int(input())
    arr.append(a)
avg = sum(arr)//5
mid = sorted(arr)[2]

print(avg)
print(mid)