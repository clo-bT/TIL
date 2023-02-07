
# s,l,r이 각각 무엇을 나타내는지 확인
# s는 판단할 단어
# l은 0부터 한바퀴 돌때마다 1씩 더해지고
# r은 한바퀴돌때마다 1씩 작아져
def recursion(s, l, r):
    print(l, r)
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l + 1, r - 1)
    

def isPalindrome(s):    
    return recursion(s, 0, len(s) - 1)

print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))
print('AAA:', isPalindrome('AAA'))
