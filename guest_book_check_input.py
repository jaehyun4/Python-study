#파일 직접 입력하는 버전
def text_counter():
    count = 0
    for i in range(len(phone_number)):
        if phone_number[i] == "-":
            count = count + 1
        else:
            continue
    return count

def text_save(guest_book):
    a = open("guest_book.txt", "w")
    a.write(guest_book)
    a.close()

guest_book = input("방명록을 넣으시오 :")
text_save(guest_book)
guest_book = open("guest_book.txt")
for line in guest_book:
    name = line[:3]
    phone_number = line[4:].rstrip()
    count = text_counter()


    if phone_number.startswith("010") != True:
        print("잘못 쓴 사람", name)
        print("잘못 쓴 번호", phone_number)
    elif len(phone_number) != 13:
        print("잘못 쓴 사람", name)
        print("잘못 쓴 번호", phone_number)
    elif count != 2:
        print("잘못 쓴 사람", name)
        print("잘못 쓴 번호", phone_number)
    else:
        continue
