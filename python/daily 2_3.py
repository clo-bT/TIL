str_lst = list(input('문자열을 입력하세요. : ').lower().split())

a = 0
print(str_lst)
b = int(len(str_lst))
for i in range (b):
    if (str_lst[i][-1] == str_lst[i+1][0]):
        a += 1
        if a == b - 1:
            print('Pass')
            break
    else:
        print('Fail')
        break



    

