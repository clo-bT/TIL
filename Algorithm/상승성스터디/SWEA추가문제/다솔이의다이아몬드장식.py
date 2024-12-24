T = int(input())#2
for tc in range(1,T+1):
    word = input() #APPLE
    if len(word)>=1:
        N = len(word)*5 - (len(word)-1)
        arr = [['.'] * N for _ in range(5)]
        for i in range(5):
            for j in range(N):
                if i % 4 == 2 and j % 4 ==2:
                    arr[i][j] = word[j//4]
                    for di,dj in [[0,-2],[-1,-1],[-2,0],[-1,1],[0,2],[1,1],[2,0],[1,-1]]:
                        arr[i+di][j+dj] = '#'
        for i in arr:
            for j in i:
                print(j,end="")
            print()