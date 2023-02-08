T = int(input()) #10
li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T+1):
    a, N = input().split() # a = #1, N = 7041
    li_input = input().split()
    li_new = []
    for i in li:
        for j in li_input:
            if i == j:
                li_new.append(j)
    print(a, *li_new)