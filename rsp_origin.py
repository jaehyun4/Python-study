import random
computer = random.choice(['가위', '바위', '보'])
my = input("가위, 바위, 보 중 하나를 입력하세요 : ")
print("나 :" , my)
print("컴퓨터 : ", computer)

if my == "가위":
    if computer == "가위":
        print("무승부")
    elif computer == "바위":
        print("패배")
    elif computer == "보":
        print("승리")
elif my == "바위":
    if computer == "가위":
        print("승리")
    elif computer == "바위":
        print("무승부")
    elif computer == "보":
        print("패배")
elif my == "보":
    if computer == "가위":
        print("패배")
    elif computer == "바위":
        print("승리")
    elif computer == "보":
        print("무승부")
