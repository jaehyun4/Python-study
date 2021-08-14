def make_comma():
    length = len(number)
    new_number = "" #new_number 생성
    if length % 3 == 1: #첫 , 앞에 있는 숫자가 1개
        for i in range(length):
            if i % 3 == 1: # number[3 * i + 1]번 째 수 앞자리에 , 추가
                new_number = new_number + "," + number[i]
            else: # [3 * i + 1]번 째가 아닌 경우에는 그냥 숫자를 뒤로 붙임
                new_number = new_number + number[i]
    elif length % 3 == 2:
            for i in range(length):
                if i % 3 == 2:
                    new_number = new_number + "," + number[i]
                else:
                    new_number = new_number + number[i]
    elif length % 3 == 0:
            for i in range(length):
                if i == 0:
                    new_number = new_number + number[i]
                elif i % 3 == 0:
                    new_number = new_number + "," + number[i]
                else:
                    new_number = new_number + number[i]
    print(new_number)

number = input("숫자를 입력하세요 : ")

while True: #잘못된 입력을 받으면 재입력 받게하는 루프
    if number.isnumeric() != True:
        print("숫자가 아닙니다!")
        number = input("숫자를 입력하세요 :")
    else:
        break

make_comma()
