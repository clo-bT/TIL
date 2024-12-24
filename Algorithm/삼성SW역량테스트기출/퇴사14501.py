T = int(input())
arr = [[list(map(int,input().split()))] for _ in range(T)]
dp = [0] * (T+1)
