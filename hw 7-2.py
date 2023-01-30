class Doggy():
    birth_of_dogs = 0
    num_of_dogs = 0

    # 초기화 메서드는 인자로 개의 이름과 견종을 받아
    def __init__(self, name, breed):
        # 인스턴스 변수에 할당
        self.name = name
        self.breed = breed
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1

    # 호출하면 개는 짖는다.
    @staticmethod
    def bark():
        print('멍')

    def __del__(self):
        Doggy.num_of_dogs -= 1

    # class 메서드를 사용하지만 self를 안받으니까 classmethod이고 
    # self 대신에 cls적고 Doggy가 cls 인거야
    @classmethod
    def get_status(cls):
        print(f'태어난 개:{cls.birth_of_dogs}, 현재 있는 개:{cls.num_of_dogs}' )

nakyeong = Doggy('쁘니', '말티즈')
hyeonhye = Doggy('콩이', '말티즈')
seunghee = Doggy('개똥이', '돼지')

del seunghee
Doggy.get_status()