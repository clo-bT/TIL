# N = int(input()) #27
# def star():
#     pass

'''
#구글링

def draw_star(num):
    global Map
 
    if num == 3: # 3X3짜리 별 하나
        Map[0][:3], Map[2][:3] = ['*', '*', '*'], ['*', '*', '*']
        Map[1][:3] = ['*', ' ', '*']
        return
    
    a = num//3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: # 가운데 공백
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*j+a] = Map[k][0:a] # 핵심!!
 
 
if __name__ == '__main__':
    N = int(input())
    # NxN 리스트 생성
    Map = [[' ' for i in range(N)] for i in range(N)]
    
    draw_star(N)
    
    # 최종 별 찍기 출력
    for i in Map:
        for j in i:
            print(j,end='')
        print('')
'''