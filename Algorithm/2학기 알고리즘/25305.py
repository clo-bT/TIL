import sys
input = sys.stdin.readline

N, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
print(arr[N-k])