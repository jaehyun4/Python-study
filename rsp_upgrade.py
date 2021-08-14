number_of_games = input("몇 판을 하시겠어요? :")
if number_of_games.isnumeric() == True:
#isnumeric()은 문자열이 숫자로 되어있는지 확인하는 함수, 숫자면 true 아니면 false
    number_of_games = int(number_of_games)
else:
    print("잘못된 입력입니다. 재입력해주세요.")
    quit()

my_win = 0
my_lose = 0
my_draw = 0
com_win = 0
com_lose = 0
com_draw = 0

import random

for i in range(1, number_of_games+1):
    computer = random.choice(['가위', '바위', '보'])
    my = input("가위, 바위, 보 중 하나를 입력하세요 : ")
    print("나 :" , my)
    print("컴퓨터 : ", computer,"\n")

    if my == computer:
        print(i, "번 째 판 무승부","\n")
        my_draw = my_draw + 1
        com_draw = com_draw + 1
    elif my == "가위":
        if computer == "바위":
            print(i, "번 째 판 패배","\n")
            my_lose = my_lose + 1
            com_win = com_win + 1
        elif computer == "보":
            print(i, "번 째 판 승리","\n")
            my_win = my_win + 1
            com_lose = com_lose + 1
    elif my == "바위":
        if computer == "가위":
            print(i, "번 째 판 승리","\n")
            my_win = my_win + 1
            com_lose = com_lose + 1
        elif computer == "보":
            print(i, "번 째 판 패배","\n")
            my_lose = my_lose + 1
            com_win = com_win + 1
    elif my == "보":
        if computer == "가위":
            print(i, "번 째 판 패배","\n")
            my_lose = my_lose + 1
            com_win = com_win + 1
        elif computer == "바위":
            print(i, "번 째 판 승리","\n")
            my_win = my_win + 1
            com_lose = com_lose + 1

print("\n")
print("나의 전적 :", my_win, "승", my_draw, "무", my_lose, "패")
print("컴퓨터의 전적 :", com_win, "승", com_draw, "무", com_lose, "패")
