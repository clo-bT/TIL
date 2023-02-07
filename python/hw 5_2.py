# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar
# dictionary 만들어 놓고
a = {}
#요일 비교해서 빼낼 리스트
b = ['월요일', '화요일','수요일','목요일','금요일','토요일','일요일']
#년도 받고 윤년인지 파악
while True:
    y = int(input())
    if (y%100 != 0 and y%4 == 0) or y%400 == 0:
        print('윤년입니다. 연도를 다시 입력해주세요.')
        continue
    
    #윤년 아니면 캘린더 보여주고
    else:
        print(calendar.calendar(y))
        a['년'] = y
        pass
    #월 일 받고 다 dict에 넣고
    m = int(input())
    d = int(input())
    a['월'] = m
    a['일'] = d
    
    #월요일이면 경고 아니면 무슨요일인지 해서 출력
    if calendar.weekday(y,m,d) == 0:
        print('경고 월요일입니다')
    
    a['요일'] = b[calendar.weekday(y,m,d)]
    print(a)
    break



