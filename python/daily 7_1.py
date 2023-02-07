# 선언을 해주고
class Nationality:
    # 초기화 (생성자)
    def __init__(self, nationality):
        # 인스턴스 변수 선언
        self.nationality = nationality
    
    # 참고) 매직 매서드 재정의
    # 재정의 : 기존에 있던 함수를 "덮어쓰기" 하는 동작
    # 원래 Nationality 객체가 가지고 있는 __str__함수가 아닌, 
    # 내가 새로 정의한 __str__ 를 호출한다.
    # 말 그대로 덮어쓰기야.
    def __str__(self):
        return '나의 국적은 ' + self.nationality
        # 대한민국을 가지고 있는 게 self.nationality 야


korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국


# 참고) 매직 메서드 등 모든 객체의 정보 출력 
print(dir(korea_nationality))