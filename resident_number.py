def personal_imformation(resident_number):
    year = resident_number[:2]
    month = resident_number[2:4]
    if resident_number[7] == 1 or 3:
        gender = "남자"
    elif resident_number[7] == 2 or 4:
        gender = "여자"
    print(year,"년",month,"월생",gender,"입니다.")

def re_input():
    print("잘못된 입력입니다.")
    global resident_number #resident_number를 전역변수로 사용
    resident_number = input("주민등록번호를 다시 입력하세요 :")

resident_number = input("주민등록번호를 입력하세요 :")

while True:
    if len(resident_number) != 14: #글자 수 14개인지
        re_input()
    elif resident_number[6] != "-" or resident_number[7] not in ["1","2","3","4"]: # 주민번호 앞자리와 뒷자리 사이에 -가 있는지, 뒷자리의 첫글자가 1 2 3 4 인지
        re_input()
    elif resident_number[:6].isnumeric() != True or resident_number[8:].isnumeric() != True: # -를 제외한 모든 자리가 숫자인지
        re_input()
    elif int(resident_number[4:6]) > 31: # 앞자리 날짜부분이 31일 이내인지
        re_input()
    elif int(resident_number[:2])<=21: # 앞자리 연도가 21이하 인지
        answer = input("2000년 이후 출생자입니까? 맞으면 1, 틀리면 2 를 입력하세요.")
        if answer != "1":
            re_input()
        else:
            if resident_number[7] != "3" and resident_number[7] != "4": #주민번호 뒷자리의 첫 글자가 3, 4인지
                re_input()
            else:
                personal_imformation(resident_number)
                break
    else:
        if resident_number[7] != "1" and resident_number[7] != "2": # 주민번호 뒷자리의 첫 글자가 1, 2 인지
            re_input()
        else:
            personal_imformation(resident_number)
            break
