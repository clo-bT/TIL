T = int(input()) #1
for tc in range(1, T+1):
    N = int(input()) #3
    for i in range(1, N+1):
        n,s,e = map(int(input().split())) #1 2 5
        # 1 일반은 모든 정류장
        # 2 급행은 짝-짝 홀-홀
        # 3 광역급행은 짝-4의배수 홀-3의배수O 10의배수X
        li = [0] * (e-s+1)
        if n == 1: #[2,3,4,5]
            for j in range():
                pass
        elif n ==2: #[3,5,7,9,10]
            if s % 2 == 0: #짝
                

                pass
            else: #홀
                pass
        elif n ==3: #[2,4,8,9]
            if s % 2 == 0: #짝
                pass
            else: #홀
                pass

'''
[0,0,1,1,1,1,0,0,0,0,0]
[0,0,0,1,0,1,0,1,0,1,1]
[0,0,1,0,1,0,0,0,1,1,0]
[0,0,2,2,2,2,0,1,1,2,1]
'''