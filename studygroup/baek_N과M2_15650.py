## 민웅님 도움
# N, M = map(int,input().split()) # 4 2
# result = []
arr = [1,2,3,4,5]
# for i in range(N):
#     arr[i] = i+1 #[1,2,3,4]
def minwoong(m,li):
    ans = []
    if len(li) < m:
        return
    if m == 1:
        for value in li:
            ans.append([value])
    else:
        for i in range(len(li)-m+1):
            for j in minwoong(m-1, li[i+1:]):
                ans.append([li[i]]+j) 

    return ans

a = minwoong(3, arr)


