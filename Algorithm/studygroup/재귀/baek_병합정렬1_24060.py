A, K = map(int,input().split()) #5 7
arr = list(map(int,input().split()))
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    # while문이 이해가 되다 말음..
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    # 위에서 비교해서 넣고 남은 거 넣어
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

new_arr = merge_sort(arr)
print(new_arr[K % A])