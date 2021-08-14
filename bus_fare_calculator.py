def bus_fare(age, pay_type):

    if age < 8:
        print("무료입니다.")
    elif age < 14:
        if pay_type == "card":
            print("450원 입니다.")
        elif pay_type == "cash":
            print("450원 입니다.")
        else:
            print("둘 다 450원 입니다.")
    elif age < 20:
        if pay_type == "card":
            print("720원 입니다.")
        elif pay_type == "cash":
            print("1000원 입니다.")
        else:
            print("카드는 720원, 현금은 1000원 입니다.")
    elif 20 <= age < 75:
            if pay_type == "card":
                print("1200원 입니다.")
            elif pay_type == "cash":
                print("1300원 입니다.")
            else:
                print("카드는 1200원, 현금은 1300원 입니다.")
    else:
            if pay_type == "card":
                print("무료입니다.")
            elif pay_type == "cash":
                print("무료입니다.")
            else:
                print("무료입니다.")

age = int(input("나이를 입력하세요 : "))
pay_type = input("결제 방식을 입력하세요(card, cash, 둘 다 확인하고 싶으면 아무거나 누르세요.) : ")

bus_fare(age, pay_type)
