# 가위바위보 게임 틀 구현
import random
# 필요한 변수 선언 (가위바위보 리스트, 컴퓨터/유저 승 카운트)
li = [ '가위', '바위', '보' ]
computer_win_count = 0
user_win_count = 0
game = 1

# 종료하기를 입력하거나 5판 하기 전까지 무한반복
while True:
    menu = int(input('가위바위보 게임을 시작합니다 !\n메뉴를 선택하세요! (1: 게임하기, 2:종료하기): '))
	# 5판 후에는 반복문 종료
    

	# 게임하기
    if menu == 1:
        while True:
            x = random.randint(1,3)
            user = int(input(f'{game}번째 게임!\n어떤 것을 내실래요? (1. 가위 / 2. 바위 / 3. 보) : '))
            rsp_list = [x,user]
            
            #이긴 경우
            if rsp_list == [1,2] or rsp_list == [2,3] or rsp_list == [3,1]:
                user_win_count += 1
                print(f'유저의 승리!\n현재 컴퓨터: {computer_win_count}승 / 유저: {user_win_count}승 입니다\n')

            #진 경우
            elif rsp_list == [2,1] or rsp_list == [3,2] or rsp_list == [1,3]:
                computer_win_count += 1
                print(f'컴퓨터의 승리!\n현재 컴퓨터: {computer_win_count}승 / 유저: {user_win_count}승 입니다\n')

            #비긴 경우
            elif rsp_list == [1,1] or rsp_list == [2,2] or rsp_list == [3,3]:
                print(f'비겼습니다!\n현재 컴퓨터: {computer_win_count}승 / 유저: {user_win_count}승 입니다\n')
            #엉뚱한 거 낸 경우
            else:
                print('다시 선택하세요\n')
                game -= 1
            #다섯번  경기 후에 종료
            if game == 6:
                break
            game += 1
        #다섯번 후에 결과로 승패 결정
        if computer_win_count > user_win_count:
            print('컴퓨터가 이겼습니다! \n프로그램을 종료합니다')
        elif computer_win_count < user_win_count:
            print('유저가 이겼습니다! \n프로그램을 종료합니다')
        else:
            print('비겼습니다!\n 프로그램을 종료합니다')
        break
                
    
	# 종료하기
    elif menu == 2:
        print('프로그램을 종료합니다')
        break

	# 잘못된 입력 - 안내문 표시 후 다시 반복
    else:
        print('다시 입력하세요')
        pass
    










