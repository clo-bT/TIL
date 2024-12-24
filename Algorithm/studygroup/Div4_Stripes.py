t = int(input())
for tc in range(1,t+1):
    # blank = input()
    arr = [input() for _ in range(8)] # 리스트 받았어
    for i in arr:
        if i == 'RRRRRRRR':
            print('R')
        elif i == 'BBBBBBBB':
            print('B')
    
    arr_t = list(zip(*arr)) # 행열 바꾸기
    for i in arr_t:
        if i == 'RRRRRRRR':
            print('R')
        elif i == 'BBBBBBBB':
            print('B')