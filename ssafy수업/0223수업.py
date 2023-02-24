'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(i):
    if i:
        print(i, end = ' ')     #중위순회 후위순회는 프린트문만 바꿔주면 돼
        preorder(left[i])
        preorder(right[i])
    return

V = int(input())
arr = list(map(int,input().split()))
E = V -1
left = [0] * (V + 1)            # 부모인덱스로 왼쪽자식 저장
right = [0] * (V + 1)           # 부모인덱스로 왼쪽자식 저장
par = [0] * (V + 1)             # 자식인덱스로 부모 저장
# child = [[] for _ in range(V+1)] # 이렇게도 저장 가능
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
    #child[p].append(c)
root = 1
while par[root] != 0:           # 루트 찾기
    root += 1








# 최대 100개의 key
# 최대힙

def enq(n): # 넣는 거
    global last
    last += 1           # 완전이진트리에 마지막 정점을 추가하고
    heap[last] = n      # 마지막 정점에 저장
    c = last            # 부모가 있고, 부모 > 자식 조건 검사를 위해
    p = c//2
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p           # 옮긴 자리에서 부모와 비교하기 위해
        p = c//2
    return

heap = [0] * 101        # 완전이진트리 1번-100번 인덱스 준비
last = 0                # 완전이진트리의 마지막 정점 번호

def deq():  # 꺼내는 거
    global last
    tmp = heap[1]       # 루트 임시저장
    heap[1] = heap[last]# 마지막 정점의 값을 루트로 이동
    last -= 1           # 마지막 정점 삭제
    p = 1
    c = p * 2           # 왼쪽자식번호
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고 오른쪽 자식의 키가 더 크면
            c += 1                              # 비교 대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:                   # 자식이 부모보다 크면
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp




enq(5)
print(heap[1])          # 루트