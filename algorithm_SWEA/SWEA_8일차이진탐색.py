## 민석님 코드 참고

def f(n):
    global i
    if n <= N:
        f(n*2)#왼쪽 노드 끝까지 재귀로 들어갔다가
        tree[n] = i # 제일 밑까지 가서 return하면(제일왼쪽자식)1부터넣고 제일 밑이라 바로 부모로 갈예정
        i += 1 # 숫자 하나 커지고
        f(n*2+1) #부모에다 i=2 넣고 빠져나온 다음에 여기 들어가서 그때의 i=3 넣음. 그럼또 빠져나와서 if문 가


T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) # 6 8 15 정점의 개수
    i = 1   # 트리에 넣을 수
    tree = [0] * (N+1)
    f(1)
    print(f'#{tc}',tree[1],tree[N//2])
    # 루트(노드번호n = 1), N 부모노드

'''
# 배열 아닌 변수 활용
# 다른 풀이 from 교수님

def f(i, a, N): # a 첫번째 왼쪽 조상의 값
    if i > N:
        return 0
    else:
        l = f(i*2, a, N)    # 왼쪽 서브트리로 갈때는 a전달
        tree[i] = l+a+1
        r = f(i*2+1, tree[i], N) # 오른쪽 서브트리고 갈때는 i가 왼쪽 조상
        return l+r+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    f(1, 0, N)
    print(f'#{tc} {tree[1]} {tree[N//2]} {tree}')
'''