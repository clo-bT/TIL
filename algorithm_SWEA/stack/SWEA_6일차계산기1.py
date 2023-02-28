## 혜진님 코드
'''
for tc in range(1, 11):
    N = int(input())
    a = list(input())
    stack = []
    temp = []
 
    for x in a:
        if '0' <= x <= '9':
            temp.append(int(x))
        else:
            if len(stack) < 1:
                stack.append(x)     # push
            else:
                stack.pop()         # pop
                stack.append(x)
                temp.append(temp.pop() + temp.pop())       # temp에 있던 요소 pop과 합 동시에. 신기
 
    while stack:                # 스택이 빌 때까지
        stack.pop()
        temp.append(temp.pop() + temp.pop())
 
    print(f'#{tc}', *temp)
'''

## 교수님 코드
'''
2+3*4/5
'''
op = {'+':1, '-':1, '*':2, '/':2}
 
def postfix(li):
    stack = [0]*len(li)
    top = -1
    pfix = ''
 
    for t in li:
        if '0' <= t <= '9':
            pfix += t
        elif t in op:
            if top == -1 or op[stack[top]] < op[t]:
                top += 1
                stack[top] = t
            else:
                while top > -1 and op[stack[top]] >= op[t]:
                    top -= 1
                    pfix += stack[top + 1]
                top += 1
                stack[top] = t
    while top > -1:
        top -= 1
        pfix += stack[top+1]
 
    return pfix
 
def postfix_eval(text):
    stack = []
    o_li = list(map(str, text))
    for i in range(len(o_li)):
        if o_li[i].isdigit():
            stack.append(int(o_li[i]))
        else:
            if len(stack) > 1 and type(stack[-1]) == int:
                a = stack.pop()
                b = stack.pop()
                if o_li[i] == '+':
                    stack.append(b+a)
                elif o_li[i] == '-':
                    stack.append(b-a)
                elif o_li[i] == '*':
                    stack.append(b*a)
                else:
                    stack.append(b//a)
 
    return stack
 
 
for tc in range(1, 11):
    N = int(input())
    op_li = list(map(str, input()))
    stack = []
 
    post = postfix(op_li)
    result = postfix_eval(post)
    print(f'#{tc} {result[0]}')
